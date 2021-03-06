#!/usr/bin/env python3

import sys
import os
import argparse
import logparser
from reporter import ReporterFactory, UnimplementedReporterException


def main():
    parser = argparse.ArgumentParser(
        usage="huokangoldlogparser.py -i HuokanGoldLogger.lua"
    )
    parser.add_argument(
        "-i",
        "--input",
        nargs="+",
        type=lambda file: file
        if os.path.isfile(file)
        else parser.error("The specified file does not exist."),
    )
    parser.add_argument(
        "-o", "--output", type=argparse.FileType("w"), default=sys.stdout
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        choices=["csv", "json", "text"],
        default="json",
    )
    parser.add_argument(
        "-t", "--type", type=str, choices=["raw", "weekly"], default="raw"
    )
    args = parser.parse_args()

    logs = map(lambda file: logparser.parse_log_file(file), args.input)
    log = logparser.merge_logs(logs)
    try:
        reporter = ReporterFactory.create_reporter(args.type, args.format, log)
        args.output.write(reporter.generate_report())
        args.output.write("\n")
    except UnimplementedReporterException as ex:
        sys.stderr.write(ex.args[0])
        sys.stderr.write("\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
