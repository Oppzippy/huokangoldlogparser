from .weeklyreporter import WeeklyReporter


class CSVWeeklyReporter(WeeklyReporter):
    def _get_time_filtered_report(
        self, total: int, gainByEvent: dict, lossByEvent: dict
    ):
        report = []
