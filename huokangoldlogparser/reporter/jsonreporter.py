import json
from .reporter import Reporter


class JSONReporter(Reporter):
    def generate_report(self):
        return json.dumps(self._log)
