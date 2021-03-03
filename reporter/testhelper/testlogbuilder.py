from datetime import datetime, timedelta, timezone


class TestLogBuilder:
    def __init__(self):
        self.money = 5_000_000_00_00  # 5m gold
        self.set_week(0)

    def create_event(self, type: str, change: int):
        timestamp = self.datetime + timedelta(minutes=self.offset)
        self.offset += 1
        prev_money = self.money
        self.money += change
        return {
            "character": {"name": "Testname", "realm": "Testrealm"},
            "type": type,
            "prevMoney": prev_money,
            "newMoney": self.money,
            "timestamp": timestamp.isoformat(),
        }

    def set_week(self, week: int):
        self.datetime = self._week_datetime(week)
        self.offset = 0

    def _week_datetime(self, week: int):
        start = datetime(2021, 1, 4, tzinfo=timezone.utc)  # First monday of 2021
        if week >= 0:
            return start + timedelta(weeks=week)
        raise Exception("week must be >= 0")
