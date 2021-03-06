from typing import List
from .testlogbuilder import TestLogBuilder


def create_test_log() -> List[dict]:
    builder = TestLogBuilder()
    builder.set_week(0)
    log = [
        builder.create_event("LOOT", change=10_00_00),
        builder.create_event("LOOT", change=15_01_25),
        builder.create_event("AUCTION_HOUSE_SELL", change=150_000_00_00),
        builder.create_event("AUCTION_HOUSE_COMMODITY_BUY", change=-200_000_00_00),
        builder.create_event("AUCTION_HOUSE_BID", change=-50_000_00_00),
        builder.create_event("TRADE", change=50_00_00),
        builder.create_event("TRADE", change=-50_00_00),
        builder.create_event("GUILD_BANK_WITHDRAW", change=1_000_000_00_00),
        builder.create_event("GUILD_BANK_DEPOSIT", change=-500_000_00_00),
        builder.create_event("MAIL_IN", change=75_53_23),
        builder.create_event("MAIL_OUT", change=-50_00_00),
    ]
    builder.set_week(3)
    log.extend([builder.create_event("BMAH_BID", change=-10_000_00_00)])

    return log
