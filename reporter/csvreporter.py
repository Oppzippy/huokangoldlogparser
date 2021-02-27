import io
import csv
from .reporter import Reporter


class CSVReporter(Reporter):
    def generate_report(self):
        output = io.StringIO()
        writer = csv.DictWriter(
            output,
            fieldnames=["Timestamp", "Event", "Previous Money", "New Money", "Change"],
        )
        writer.writeheader()
        for event in self._log:
            moneyDiff = event["newMoney"] - event["prevMoney"]
            writer.writerow(
                {
                    "Timestamp": event["timestamp"],
                    "Event": event["type"],
                    "Previous Money": event["prevMoney"],
                    "New Money": event["newMoney"],
                    "Change": moneyDiff,
                }
            )
        return output.getvalue()
