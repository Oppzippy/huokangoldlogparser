from functools import reduce
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
from typing import List
import dateutil.parser
from .reporter import Reporter


class WeeklyReporter(Reporter, ABC):
    def __init__(self, log: List[dict]):
        super().__init__(log)
        self._log = log

    def generate_report(self) -> str:
        if len(self._log) == 0:
            return None
        first_date = dateutil.parser.isoparse(self._log[0]["timestamp"])
        last_date = dateutil.parser.isoparse(self._log[-1]["timestamp"])
        reports = []
        # TODO improve performance
        # We're currently filtering the entire log for every individual week
        # Since the log is sorted, we only need to look at what comes after the previous
        # end index.
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
        self, start_date: datetime, gain_by_event: dict, loss_by_event: dict
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
    def _gain_by_event_type(cls, log: List[dict]):
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
    def _loss_by_event_type(cls, log: List[dict]):
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


def iterate_weeks(start_date: datetime, end: datetime):
    start_date = start_date - timedelta(start_date.weekday())
    start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
    current_date = start_date
    while current_date <= end:
        next_date = current_date + timedelta(weeks=1)
        yield (current_date, next_date)
        current_date = next_date


def sum_change(log: List[dict]):
    return reduce(
        lambda acc, event: acc + (event["newMoney"] - event["prevMoney"]), log, 0
    )
