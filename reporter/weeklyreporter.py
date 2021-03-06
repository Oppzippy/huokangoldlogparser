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
        reports = []
        for filtered_log in self._weekly_logs():
            week_start = _first_day_of_week(
                dateutil.parser.isoparse(filtered_log[0]["timestamp"])
            )
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

    def _weekly_logs(self):
        if len(self._log) == 0:
            return
        # The log is sorted so we know there will be no more relevant entries
        # after we find one outside of our target time period
        current_end = _last_day_of_week(
            dateutil.parser.isoparse(self._log[0]["timestamp"])
        )
        start_index = 0
        for i in range(1, len(self._log)):
            event = self._log[i]
            timestamp = dateutil.parser.isoparse(event["timestamp"])
            if timestamp >= current_end:
                yield self._log[start_index:i]
                current_end = _last_day_of_week(timestamp)
                start_index = i
        yield self._log[start_index:]

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


def _first_day_of_week(day: datetime):
    first_day = day - timedelta(day.weekday())
    return first_day.replace(hour=0, minute=0, second=0, microsecond=0)


def _last_day_of_week(day: datetime):
    first_day = _first_day_of_week(day)
    return first_day + timedelta(weeks=1)
