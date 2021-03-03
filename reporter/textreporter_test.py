import unittest
from .textreporter import TextReporter
from .testhelper import create_test_log


class TextReporterTest(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.max_diff = None

    def test_report(self):
        log = create_test_log()
        reporter = TextReporter(log)
        report = reporter.generate_report()
        self.assertEqual(
            report,
            """\
2021-01-04T00:00:00+00:00: Testname-Testrealm gained 10g from LOOT.
2021-01-04T00:01:00+00:00: Testname-Testrealm gained 15g from LOOT.
2021-01-04T00:02:00+00:00: Testname-Testrealm gained 150,000g from AUCTION_HOUSE_SELL.
2021-01-04T00:03:00+00:00: Testname-Testrealm lost 200,000g from AUCTION_HOUSE_COMMODITY_BUY.
2021-01-04T00:04:00+00:00: Testname-Testrealm lost 50,000g from AUCTION_HOUSE_BID.
2021-01-04T00:05:00+00:00: Testname-Testrealm gained 50g from TRADE.
2021-01-04T00:06:00+00:00: Testname-Testrealm lost 50g from TRADE.
2021-01-04T00:07:00+00:00: Testname-Testrealm gained 1,000,000g from GUILD_BANK_WITHDRAW.
2021-01-04T00:08:00+00:00: Testname-Testrealm lost 500,000g from GUILD_BANK_DEPOSIT.
2021-01-04T00:09:00+00:00: Testname-Testrealm gained 75g from MAIL_IN.
2021-01-04T00:10:00+00:00: Testname-Testrealm lost 50g from MAIL_OUT.""",
        )
