from .csvreporter import CSVReporter
from .jsonreporter import JSONReporter
from .textreporter import TextReporter
from .csvweeklyreporter import CSVWeeklyReporter
from .jsonweeklyreporter import JSONWeeklyReporter
from .textweeklyreporter import TextWeeklyReporter
from .exceptions import UnimplementedReporterException

CLASS_MAP = {
    "raw": {
        "csv": CSVReporter,
        "json": JSONReporter,
        "text": TextReporter,
    },
    "weekly": {
        "csv": CSVWeeklyReporter,
        "json": JSONWeeklyReporter,
        "text": TextWeeklyReporter,
    },
}


class ReporterFactory:
    @classmethod
    def create_reporter(cls, type_: str, format_: str, log: list):
        if type_ in CLASS_MAP and format_ in CLASS_MAP[type_]:
            return CLASS_MAP[type_][format_](log)
        raise UnimplementedReporterException(
            f"Reporter of type {type_} and format {format_} is not implemented."
        )
