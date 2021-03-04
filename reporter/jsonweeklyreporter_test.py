import unittest
import json
from .jsonweeklyreporter import JSONWeeklyReporter
from .testhelper import create_test_log


class JSONWeeklyReporterTest(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        # pylint: disable=invalid-name
        self.maxDiff = None

    def test_report(self):
        log = create_test_log()
        reporter = JSONWeeklyReporter(log)
        report = reporter.generate_report()
        parsed_report = json.loads(report)
        self.assertListEqual(
            parsed_report,
            [
                {
                    "weekStartTimestamp": "2021-01-04T00:00:00+00:00",
                    "report": {
                        "LOOT": {
                            "gain": 250125,
                            "loss": 0,
                        },
                        "AUCTION_HOUSE_SELL": {
                            "gain": 1500000000,
                            "loss": 0,
                        },
                        "AUCTION_HOUSE_COMMODITY_BUY": {
                            "gain": 0,
                            "loss": 2000000000,
                        },
                        "AUCTION_HOUSE_BID": {
                            "gain": 0,
                            "loss": 500000000,
                        },
                        "TRADE": {
                            "gain": 500000,
                            "loss": 500000,
                        },
                        "GUILD_BANK_WITHDRAW": {
                            "gain": 10000000000,
                            "loss": 0,
                        },
                        "GUILD_BANK_DEPOSIT": {
                            "gain": 0,
                            "loss": 5000000000,
                        },
                        "MAIL_IN": {
                            "gain": 755323,
                            "loss": 0,
                        },
                        "MAIL_OUT": {
                            "gain": 0,
                            "loss": 500000,
                        },
                    },
                },
            ],
        )
