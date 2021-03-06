import unittest
from .csvweeklyreporter import CSVWeeklyReporter
from .testhelper import create_test_log


class CSVWeeklyReporterTest(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        # pylint: disable=invalid-name
        self.maxDiff = None

    def test_empty_report(self):
        reporter = CSVWeeklyReporter([])
        report = reporter.generate_report()
        self.assertEqual(report, "Week,Event,Gain,Loss")

    def test_report(self):
        log = create_test_log()
        reporter = CSVWeeklyReporter(log)
        report = reporter.generate_report()
        lines = report.splitlines()
        header, *entries = lines
        self.assertEqual(header, "Week,Event,Gain,Loss")
        self.assertSetEqual(
            set(entries),
            set(
                [
                    "2021-01-04,LOOT,250125,0",
                    "2021-01-04,AUCTION_HOUSE_SELL,1500000000,0",
                    "2021-01-04,AUCTION_HOUSE_COMMODITY_BUY,0,2000000000",
                    "2021-01-04,AUCTION_HOUSE_BID,0,500000000",
                    "2021-01-04,TRADE,500000,500000",
                    "2021-01-04,GUILD_BANK_WITHDRAW,10000000000,0",
                    "2021-01-04,GUILD_BANK_DEPOSIT,0,5000000000",
                    "2021-01-04,MAIL_IN,755323,0",
                    "2021-01-04,MAIL_OUT,0,500000",
                    "2021-01-25,BMAH_BID,0,100000000",
                ]
            ),
        )
