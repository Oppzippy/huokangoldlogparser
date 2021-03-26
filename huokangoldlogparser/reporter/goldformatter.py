import locale

locale.setlocale(locale.LC_ALL, "")


def format_gold(copper: int):
    gold = copper / 10000
    return locale.format_string("%d", gold, grouping=True) + "g"
