#!/usr/bin/env python3

import sys, os, io, re
import base64
import zlib
import json
import argparse
import csv
from datetime import date, datetime, time, timedelta
import dateutil.parser
from weeklyreporter import HumanWeeklyReporter


def log_to_csv(log: list) -> str:
    output = io.StringIO()
    writer = csv.DictWriter(
        output,
        fieldnames=["Timestamp", "Event", "Previous Money", "New Money", "Change"],
    )
    writer.writeheader()
    for event in log:
        moneyDiff = event["newMoney"] - event["prevMoney"]
        writer.writerow(
            {
                "Timestamp": event["timestamp"],
                "Event": event["type"],
                "Previous Money": event["prevMoney"],
                "New Money": event["newMoney"],
                "Change": moneyDiff,
            }
        )
    return output.getvalue()


def decompress_log(log: list) -> list:
    events = []
    for entry_b64 in log:
        entry_compressed = base64.b64decode(entry_b64)
        entry_json = zlib.decompress(entry_compressed, -15)  # no deflate headers
        entry = json.loads(entry_json)
        if isinstance(entry, list):
            events.extend(entry)
        else:
            events.append(entry)
    return events


def read_log_file(file_path: str) -> list:
    with open(file_path, "r") as f:
        log = []
        readingLog = False
        for line in f:
            line = line.rstrip("\n")
            if line == "HuokanGoldLog = {":
                readingLog = True
            elif readingLog:
                if line == "}":
                    break
                string = read_log_file_line(line)
                log.append(string)
        if not readingLog:
            raise Exception("File didn't contain a log.")
        return log


def read_log_file_line(line: str) -> str:
    match = re.match(r'^\t"(.*)", -- \[\d+\]$', line)
    if match is None:
        raise Exception(f"Error parsing line: {line}")
    return match.group(1)


parser = argparse.ArgumentParser(usage="./decompress.py HuokanGoldLogger.lua")
parser.add_argument(
    "file",
    type=lambda file: file
    if os.path.isfile(file)
    else parser.error("The specified file does not exist."),
)
parser.add_argument(
    "--format", type=str, choices=["csv", "json", "summary"], default="csv"
)
args = parser.parse_args()

log = decompress_log(read_log_file(args.file))
if args.format == "json":
    print(json.dumps(log))
elif args.format == "csv":
    print(log_to_csv(log))
elif args.format == "summary":
    reporter = HumanWeeklyReporter(log)
    print(reporter.generate_report())
