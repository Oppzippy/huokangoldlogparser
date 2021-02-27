import io
import csv
from datetime import datetime
from .weeklyreporter import WeeklyReporter


class CSVWeeklyReporter(WeeklyReporter):
    def _get_time_filtered_report(
        self, startDate: datetime, gainByEvent: dict, lossByEvent: dict
    ):
        output = io.StringIO()
        writer = csv.DictWriter(
            output,
            fieldnames=["Week", "Event", "Gain", "Loss"],
        )
        allEventTypes = set(gainByEvent.keys())
        allEventTypes.union(lossByEvent.keys())
        for eventType in allEventTypes:
            writer.writerow(
                {
                    "Week": startDate.date().strftime("%Y-%m-%d"),
                    "Event": eventType,
                    "Gain": gainByEvent.get(eventType, 0),
                    "Loss": lossByEvent.get(eventType, 0),
                }
            )
        return output.getvalue()

    def _merge_filtered_reports(self, reports: list):
        output = io.StringIO()
        writer = csv.DictWriter(
            output,
            fieldnames=["Week", "Event", "Gain", "Loss"],
        )
        writer.writeheader()
        header = output.getvalue()
        return header + "".join(reports)
