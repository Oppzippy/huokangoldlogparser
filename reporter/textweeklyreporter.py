from datetime import datetime
from typing import List
from .goldformatter import format_gold
from .weeklyreporter import WeeklyReporter


class TextWeeklyReporter(WeeklyReporter):
    def _get_time_filtered_report(
        self, start_date: datetime, gain_by_event: dict, loss_by_event: dict
    ):
        report = []
        report.append(f"**Week of {start_date.strftime('%B %d, %Y')}**")
        report.append(f"Weekly Total Gain: {format_gold(sum(gain_by_event.values()))}")
        report.append(f"Weekly Total Loss: {format_gold(sum(loss_by_event.values()))}")
        report.append(
            f"Weekly AH Gain: {format_gold(gain_by_event.get('AUCTION_HOUSE_SELL', 0))}"
        )
        report.append(
            f"Weekly AH Loss: {format_gold(loss_by_event.get('AUCTION_HOUSE_BID', 0) + loss_by_event.get('AUCTION_HOUSE_COMMODITY_BUY', 0))}"
        )
        report.append(
            f"Weekly Trade Gain: {format_gold(gain_by_event.get('TRADE', 0))}"
        )
        report.append(
            f"Weekly Trade Loss: {format_gold(loss_by_event.get('TRADE', 0))}"
        )
        report.append(
            f"Weekly Guild Bank Withdraw: {format_gold(gain_by_event.get('GUILD_BANK_WITHDRAW', 0))}"
        )
        report.append(
            f"Weekly Guild Bank Deposit: {format_gold(loss_by_event.get('GUILD_BANK_DEPOSIT', 0))}"
        )
        report.append(
            f"Weekly Mail Gain: {format_gold(gain_by_event.get('MAIL_IN', 0))}"
        )
        report.append(
            f"Weekly Mail Loss: {format_gold(loss_by_event.get('MAIL_OUT', 0))}"
        )
        return "\n".join(report)

    def _merge_filtered_reports(self, reports: List[str]):
        return "\n\n".join(reports)
