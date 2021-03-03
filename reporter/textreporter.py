from .reporter import Reporter
from .goldformatter import format_gold


class TextReporter(Reporter):
    def generate_report(self):
        lines = map(lambda event: self._format_message(event), self._log)
        return "\n".join(lines)

    def _format_message(self, event: dict):
        character = event["character"]
        charater_name = f"{character['name']}-{character['realm']}"
        gold_diff = event["newMoney"] - event["prevMoney"]

        return f"{event['timestamp']}: {charater_name} {'gained' if gold_diff > 0 else 'lost'} \
{format_gold(abs(gold_diff))} from {event['type']}."
