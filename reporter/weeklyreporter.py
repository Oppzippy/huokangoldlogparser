from functools import reduce
from datetime import datetime, timedelta
import dateutil.parser
from .reporter import Reporter
from abc import ABC, abstractmethod


class WeeklyReporter(Reporter, ABC):
    def __init__(self, log: list[dict]):
        self._log = log

    def generate_report(self) -> str:
        first_date = dateutil.parser.isoparse(self._log[0]["timestamp"])
        last_date = dateutil.parser.isoparse(self._log[-1]["timestamp"])
        reports = []
        for (week_start, week_end) in iterate_weeks(first_date, last_date):
            filtered_log = self._get_time_filtered_log(week_start, week_end)
            gain_by_event = self._gain_by_event_type(filtered_log)
            loss_by_event = self._loss_by_event_type(filtered_log)
            reports.append(
                self._get_time_filtered_report(week_start, gain_by_event, loss_by_event)
            )
        return self._merge_filtered_reports(reports)

    @abstractmethod
    def _merge_filtered_reports(self, reports):
        pass

    @abstractmethod
    def _get_time_filtered_report(
        self, total: int, gain_by_event: dict, loss_by_event: dict
    ):
        pass

    def _get_time_filtered_log(self, start_date: datetime, end_date: datetime):
        return list(
            filter(
                lambda event: start_date
                <= dateutil.parser.isoparse(event["timestamp"])
                < end_date,
                self._log,
            )
        )

    @classmethod
    def _gain_by_event_type(self, log: list[dict]):
        gain_by_event_type = {}
        for event in log:
            gain = event["newMoney"] - event["prevMoney"]
            event_type = event["type"]
            if gain > 0:
                gain_by_event_type[event_type] = (
                    gain_by_event_type.get(event_type, 0) + gain
                )
        return gain_by_event_type

    @classmethod
    def _loss_by_event_type(self, log: list[dict]):
        loss_by_event_type = {}
        for event in log:
            loss = event["prevMoney"] - event["newMoney"]
            event_type = event["type"]
            if loss > 0:
                loss_by_event_type[event_type] = (
                    loss_by_event_type.get(event_type, 0) + loss
                )
        return loss_by_event_type


# Utility


def iterate_weeks(start: datetime, end: datetime):
    start = start - timedelta(start.weekday())
    start = start.replace(hour=0, minute=0, second=0, microsecond=0)
    current = start
    while current <= end:
        next = current + timedelta(weeks=1)
        yield (current, next)
        current = next


def sum_change(log: list[dict]):
    return reduce(
        lambda acc, event: acc + (event["newMoney"] - event["prevMoney"]), log, 0
    )
