import io
import csv
from datetime import datetime
from typing import List
from .weeklyreporter import WeeklyReporter


class CSVWeeklyReporter(WeeklyReporter):
    def _get_time_filtered_report(
        self, start_date: datetime, gain_by_event: dict, loss_by_event: dict
    ):
        output = io.StringIO(newline="")
        writer = csv.DictWriter(
            output, fieldnames=["Week", "Event", "Gain", "Loss"], lineterminator="\n"
        )
        all_event_types = set(gain_by_event.keys())
        all_event_types.update(loss_by_event.keys())
        for event_type in all_event_types:
            writer.writerow(
                {
                    "Week": start_date.date().strftime("%Y-%m-%d"),
                    "Event": event_type,
                    "Gain": gain_by_event.get(event_type, 0),
                    "Loss": loss_by_event.get(event_type, 0),
                }
            )
        return output.getvalue()

    def _merge_filtered_reports(self, reports: List[dict]):
        output = io.StringIO()
        writer = csv.DictWriter(
            output, fieldnames=["Week", "Event", "Gain", "Loss"], lineterminator="\n"
        )
        writer.writeheader()
        header = output.getvalue()
        return header + "".join(reports)
