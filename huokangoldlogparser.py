#!/usr/bin/env python3

import sys
import os
import argparse
import logparser
from reporter import ReporterFactory, UnimplementedReporterException


def main():
    parser = argparse.ArgumentParser(
        usage="huokangoldlogparser.py HuokanGoldLogger.lua --type=raw --format=json"
    )
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
        print(reporter.generate_report())
    except UnimplementedReporterException as ex:
        print(ex.args[0])
        sys.exit(1)


if __name__ == "__main__":
    main()
