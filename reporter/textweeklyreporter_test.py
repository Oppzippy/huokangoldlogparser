import unittest
from .textweeklyreporter import TextWeeklyReporter
from .testhelper import create_test_log


class TextWeeklyReporterTest(unittest.TestCase):
    def testReport(self):
        self.maxDiff = None
        log = create_test_log()
        reporter = TextWeeklyReporter(log)
        report = reporter.generate_report()
        self.assertEqual(
            report,
            """\
**Week of January 04, 2021**
Weekly Total Gain: 1,150,150g
Weekly Total Loss: 750,100g
Weekly AH Gain: 150,000g
Weekly AH Loss: 250,000g
Weekly Trade Gain: 50g
Weekly Trade Loss: 50g
Weekly Guild Bank Withdraw: 1,000,000g
Weekly Guild Bank Deposit: 500,000g
Weekly Mail Gain: 75g
Weekly Mail Loss: 50g""",
        )
