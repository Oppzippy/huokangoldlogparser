import unittest
from .csvreporter import CSVReporter
from .testhelper import create_test_log


class CSVReporterTest(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.max_diff = None

    def test_report(self):
        log = create_test_log()
        reporter = CSVReporter(log)
        report = reporter.generate_report()
        lines = report.splitlines()
        header, *entries = lines
        self.assertEqual(header, "Timestamp,Event,Previous Money,New Money,Change")
        self.assertSetEqual(
            set(entries),
            set(
                [
                    "2021-01-04T00:00:00+00:00,LOOT,50000000000,50000100000,100000",
                    "2021-01-04T00:01:00+00:00,LOOT,50000100000,50000250125,150125",
                    "2021-01-04T00:02:00+00:00,AUCTION_HOUSE_SELL,50000250125,51500250125,1500000000",
                    "2021-01-04T00:03:00+00:00,AUCTION_HOUSE_COMMODITY_BUY,51500250125,49500250125,-2000000000",
                    "2021-01-04T00:04:00+00:00,AUCTION_HOUSE_BID,49500250125,49000250125,-500000000",
                    "2021-01-04T00:05:00+00:00,TRADE,49000250125,49000750125,500000",
                    "2021-01-04T00:06:00+00:00,TRADE,49000750125,49000250125,-500000",
                    "2021-01-04T00:07:00+00:00,GUILD_BANK_WITHDRAW,49000250125,59000250125,10000000000",
                    "2021-01-04T00:08:00+00:00,GUILD_BANK_DEPOSIT,59000250125,54000250125,-5000000000",
                    "2021-01-04T00:09:00+00:00,MAIL_IN,54000250125,54001005448,755323",
                    "2021-01-04T00:10:00+00:00,MAIL_OUT,54001005448,54000505448,-500000",
                ]
            ),
        )
