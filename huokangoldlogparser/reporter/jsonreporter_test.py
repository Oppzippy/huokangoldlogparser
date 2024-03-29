import unittest
import json
from .jsonreporter import JSONReporter
from .testhelper import create_test_log


class JSONReporterTest(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        # pylint: disable=invalid-name
        self.maxDiff = None

    def test_report(self):
        log = create_test_log()
        reporter = JSONReporter(log)
        report = reporter.generate_report()
        parsed_report = json.loads(report)
        self.assertListEqual(
            parsed_report,
            [
                {
                    "character": {
                        "name": "Testname",
                        "realm": "Testrealm",
                    },
                    "type": "LOOT",
                    "prevMoney": 50000000000,
                    "newMoney": 50000100000,
                    "timestamp": "2021-01-04T00:00:00+00:00",
                },
                {
                    "character": {
                        "name": "Testname",
                        "realm": "Testrealm",
                    },
                    "type": "LOOT",
                    "prevMoney": 50000100000,
                    "newMoney": 50000250125,
                    "timestamp": "2021-01-04T00:01:00+00:00",
                },
                {
                    "character": {
                        "name": "Testname",
                        "realm": "Testrealm",
                    },
                    "type": "AUCTION_HOUSE_SELL",
                    "prevMoney": 50000250125,
                    "newMoney": 51500250125,
                    "timestamp": "2021-01-04T00:02:00+00:00",
                },
                {
                    "character": {
                        "name": "Testname",
                        "realm": "Testrealm",
                    },
                    "type": "AUCTION_HOUSE_COMMODITY_BUY",
                    "prevMoney": 51500250125,
                    "newMoney": 49500250125,
                    "timestamp": "2021-01-04T00:03:00+00:00",
                },
                {
                    "character": {
                        "name": "Testname",
                        "realm": "Testrealm",
                    },
                    "type": "AUCTION_HOUSE_BID",
                    "prevMoney": 49500250125,
                    "newMoney": 49000250125,
                    "timestamp": "2021-01-04T00:04:00+00:00",
                },
                {
                    "character": {
                        "name": "Testname",
                        "realm": "Testrealm",
                    },
                    "type": "TRADE",
                    "prevMoney": 49000250125,
                    "newMoney": 49000750125,
                    "timestamp": "2021-01-04T00:05:00+00:00",
                },
                {
                    "character": {
                        "name": "Testname",
                        "realm": "Testrealm",
                    },
                    "type": "TRADE",
                    "prevMoney": 49000750125,
                    "newMoney": 49000250125,
                    "timestamp": "2021-01-04T00:06:00+00:00",
                },
                {
                    "character": {
                        "name": "Testname",
                        "realm": "Testrealm",
                    },
                    "type": "GUILD_BANK_WITHDRAW",
                    "prevMoney": 49000250125,
                    "newMoney": 59000250125,
                    "timestamp": "2021-01-04T00:07:00+00:00",
                },
                {
                    "character": {
                        "name": "Testname",
                        "realm": "Testrealm",
                    },
                    "type": "GUILD_BANK_DEPOSIT",
                    "prevMoney": 59000250125,
                    "newMoney": 54000250125,
                    "timestamp": "2021-01-04T00:08:00+00:00",
                },
                {
                    "character": {
                        "name": "Testname",
                        "realm": "Testrealm",
                    },
                    "type": "MAIL_IN",
                    "prevMoney": 54000250125,
                    "newMoney": 54001005448,
                    "timestamp": "2021-01-04T00:09:00+00:00",
                },
                {
                    "character": {
                        "name": "Testname",
                        "realm": "Testrealm",
                    },
                    "type": "MAIL_OUT",
                    "prevMoney": 54001005448,
                    "newMoney": 54000505448,
                    "timestamp": "2021-01-04T00:10:00+00:00",
                },
                {
                    "character": {
                        "name": "Testname",
                        "realm": "Testrealm",
                    },
                    "type": "BMAH_BID",
                    "prevMoney": 54000505448,
                    "newMoney": 53900505448,
                    "timestamp": "2021-01-25T00:00:00+00:00",
                },
            ],
        )
