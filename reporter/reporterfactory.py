from .jsonreporter import JSONReporter
from .csvweeklyreporter import CSVWeeklyReporter
from .csvreporter import CSVReporter
from .textweeklyreporter import TextWeeklyReporter
from .exceptions import UnimplementedReporterException

classMap = {
    "raw": {
        "csv": CSVReporter,
        "json": JSONReporter,
    },
    "weekly": {
        "text": TextWeeklyReporter,
        "csv": CSVWeeklyReporter,
    },
}


class ReporterFactory:
    @classmethod
    def create_reporter(cls, type: str, format: str, log: list):
        if type in classMap and format in classMap[type]:
            return classMap[type][format](log)
        raise UnimplementedReporterException(
            f"Reporter of type {type} and format {format} is not implemented."
        )
