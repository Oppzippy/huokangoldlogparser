from functools import reduce
import locale
from datetime import date, datetime, time, timedelta
import dateutil.parser
from .weeklyreporter import WeeklyReporter

locale.setlocale(locale.LC_ALL, "")


class TextWeeklyReporter(WeeklyReporter):
    def _get_time_filtered_report(
        self, startDate: datetime, gainByEvent: dict, lossByEvent: dict
    ):
        report = []
        report.append(f"**Week of {startDate.strftime('%B %d')}**")
        report.append(
            f"Weekly Total Gain: {self._format_gold(sum(gainByEvent.values()))}"
        )
        report.append(
            f"Weekly Total Loss: {self._format_gold(sum(lossByEvent.values()))}"
        )
        report.append(
            f"Weekly AH Gain: {self._format_gold(gainByEvent.get('AUCTION_HOUSE_SELL', 0))}"
        )
        report.append(
            f"Weekly AH Loss: {self._format_gold(lossByEvent.get('AUCTION_HOUSE_BID', 0) + lossByEvent.get('AUCTION_HOUSE_COMMODITY_BUY', 0))}"
        )
        report.append(
            f"Weekly Trade Gain: {self._format_gold(gainByEvent.get('TRADE', 0))}"
        )
        report.append(
            f"Weekly Trade Loss: {self._format_gold(lossByEvent.get('TRADE', 0))}"
        )
        report.append(
            f"Weekly Guild Bank Withdraw: {self._format_gold(gainByEvent.get('GUILD_BANK_WITHDRAW', 0))}"
        )
        report.append(
            f"Weekly Guild Bank Deposit: {self._format_gold(lossByEvent.get('GUILD_BANK_DEPOSIT', 0))}"
        )
        report.append(
            f"Weekly Mail Gain: {self._format_gold(gainByEvent.get('MAIL_IN', 0))}"
        )
        report.append(
            f"Weekly Mail Loss: {self._format_gold(lossByEvent.get('MAIL_OUT', 0))}"
        )
        return "\n".join(report)

    def _format_gold(self, copper: int):
        gold = copper / 10000
        return locale.format_string("%d", gold, grouping=True) + "g"

    def _merge_filtered_reports(self, reports: list):
        return "\n\n".join(reports)
