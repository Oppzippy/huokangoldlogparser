#!/usr/bin/env python3

import sys, os, io, re
import base64
import zlib
import json
import argparse
import csv
from datetime import date, datetime, time, timedelta
import dateutil.parser
import logparser
from reporter import ReporterFactory, UnimplementedReporterException


parser = argparse.ArgumentParser(usage="./decompress.py HuokanGoldLogger.lua")
parser.add_argument(
    "file",
    type=lambda file: file
    if os.path.isfile(file)
    else parser.error("The specified file does not exist."),
)
parser.add_argument(
    "--format",
    type=str,
    choices=["csv", "json", "text"],
    default="json",
)
parser.add_argument("--type", type=str, choices=["raw", "weekly"], default="raw")
args = parser.parse_args()

log = logparser.parse_log_file(args.file)
try:
    reporter = ReporterFactory.create_reporter(args.type, args.format, log)
    sys.stdout.write(reporter.generate_report())
except UnimplementedReporterException as ex:
    print(ex.args[0])
    sys.exit(1)
