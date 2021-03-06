import re
import zlib
import base64
import json
from typing import Iterable, List
import dateutil.parser
from .exceptions import ParserException


def merge_logs(logs: Iterable[List[dict]]):
    unsorted_log = (event for log in logs for event in log)
    return sorted(
        unsorted_log, key=lambda event: dateutil.parser.isoparse(event["timestamp"])
    )


def parse_log_file(file_path: str) -> List[dict]:
    return _decompress_log(_read_log_file(file_path))


def _read_log_file(file_path: str) -> List[str]:
    with open(file_path, "r") as file_:
        log = []
        reading_log = False
        for line in file_:
            line = line.rstrip("\n")
            if line.startswith("HuokanGoldLog = {"):
                reading_log = True
            elif reading_log:
                if line == "}":
                    break
                string = _read_log_file_line(line)
                log.append(string)
        if not reading_log:
            raise ParserException("File didn't contain a log.")
        return log


def _read_log_file_line(line: str) -> str:
    match = re.match(r'^\t"(.*)", -- \[\d+\]$', line)
    if match is None:
        raise ParserException(f"Error parsing line: {line}")
    return match.group(1)


def _decompress_log(log: List[str]) -> List[dict]:
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
