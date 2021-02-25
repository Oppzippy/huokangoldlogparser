from functools import reduce
from datetime import datetime, timedelta
import dateutil.parser
from abc import ABC, abstractmethod


class WeeklyReporter(ABC):
    def __init__(self, log: list):
        self._log = log

    def generate_report(self):
        firstDate = dateutil.parser.isoparse(self._log[0]["timestamp"])
        lastDate = dateutil.parser.isoparse(self._log[-1]["timestamp"])
        reports = []
        for (weekStart, weekEnd) in iterate_weeks(firstDate, lastDate):
            filteredLog = self._get_time_filtered_log(weekStart, weekEnd)
            gainByEvent = self._gain_by_event_type(filteredLog)
            lossByEvent = self._loss_by_event_type(filteredLog)
            reports.append(
                self._get_time_filtered_report(weekStart, gainByEvent, lossByEvent)
            )
        return self._merge_filtered_reports(reports)

    @abstractmethod
    def _merge_filtered_reports(self, reports):
        pass

    @abstractmethod
    def _get_time_filtered_report(
        self, total: int, gainByEvent: dict, lossByEvent: dict
    ):
        pass

    def _get_time_filtered_log(self, startDate: datetime, endDate: datetime):
        return list(
            filter(
                lambda event: startDate
                <= dateutil.parser.isoparse(event["timestamp"])
                < endDate,
                self._log,
            )
        )

    @classmethod
    def _gain_by_event_type(self, log: list):
        gainByEventType = {}
        for event in log:
            gain = event["newMoney"] - event["prevMoney"]
            eventType = event["type"]
            if gain > 0:
                gainByEventType[eventType] = gainByEventType.get(eventType, 0) + gain
        return gainByEventType

    @classmethod
    def _loss_by_event_type(self, log: list):
        lossByEventType = {}
        for event in log:
            loss = event["prevMoney"] - event["newMoney"]
            eventType = event["type"]
            if loss > 0:
                lossByEventType[eventType] = lossByEventType.get(eventType, 0) + loss
        return lossByEventType


# Utility


def iterate_weeks(start: datetime, end: datetime):
    start = start - timedelta(start.weekday())
    start = start.replace(hour=0, minute=0, second=0, microsecond=0)
    current = start
    while current <= end:
        next = current + timedelta(weeks=1)
        yield (current, next)
        current = next


def sum_change(log: list):
    return reduce(
        lambda acc, event: acc + (event["newMoney"] - event["prevMoney"]), log, 0
    )
