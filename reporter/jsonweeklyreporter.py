from datetime import datetime
import json
from .weeklyreporter import WeeklyReporter


class JSONWeeklyReporter(WeeklyReporter):
    def _get_time_filtered_report(
        self, start_date: datetime, gain_by_event: dict, loss_by_event: dict
    ):
        event_types = set(gain_by_event.keys())
        event_types.update(loss_by_event.keys())

        event_type_gold_changes = {
            event_type: {
                "gain": gain_by_event.get(event_type, 0),
                "loss": loss_by_event.get(event_type, 0),
            }
            for event_type in event_types
        }
        return {
            "weekStartTimestamp": start_date.isoformat(),
            "report": event_type_gold_changes,
        }

    def _merge_filtered_reports(self, reports):
        return json.dumps(reports)
