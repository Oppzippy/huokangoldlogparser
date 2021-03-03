from .csvreporter import CSVReporter
from .jsonreporter import JSONReporter
from .textreporter import TextReporter
from .csvweeklyreporter import CSVWeeklyReporter
from .textweeklyreporter import TextWeeklyReporter
from .exceptions import UnimplementedReporterException

class_map = {
    "raw": {
        "csv": CSVReporter,
        "json": JSONReporter,
        "text": TextReporter,
    },
    "weekly": {
        "csv": CSVWeeklyReporter,
        "text": TextWeeklyReporter,
    },
}


class ReporterFactory:
    @classmethod
    def create_reporter(cls, type: str, format: str, log: list):
        if type in class_map and format in class_map[type]:
            return class_map[type][format](log)
        raise UnimplementedReporterException(
            f"Reporter of type {type} and format {format} is not implemented."
        )
