import unittest
from .textweeklyreporter import TextWeeklyReporter
from .testhelper import create_test_log


class TextWeeklyReporterTest(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        # pylint: disable=invalid-name
        self.maxDiff = None

    def test_empty_report(self):
        reporter = TextWeeklyReporter([])
        report = reporter.generate_report()
        self.assertEqual(report, "The report is empty.")

    def test_report(self):
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
Weekly Mail Loss: 50g

**Week of January 25, 2021**
Weekly Total Gain: 0g
Weekly Total Loss: 10,000g
Weekly AH Gain: 0g
Weekly AH Loss: 10,000g
Weekly Trade Gain: 0g
Weekly Trade Loss: 0g
Weekly Guild Bank Withdraw: 0g
Weekly Guild Bank Deposit: 0g
Weekly Mail Gain: 0g
Weekly Mail Loss: 0g""",
        )
