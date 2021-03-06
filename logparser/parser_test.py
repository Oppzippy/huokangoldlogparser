import unittest
import tempfile
from .parser import parse_log_file
from .exceptions import ParserException

EMPTY_GOLD_LOG = """
HuokanGoldLog = {
}
"""

UNCOMPRESSED_GOLD_LOG = """
HuokanGoldLog = {
	"TczNCsIwEATgd9lzhSSatMkbCEouPXlb6qKF/BGDEkrf3fUmzGnm292gVHpfc6IOzipxtFIbqacBWi8EDi7ezzBAos8/MpMctWW0Rno1jIWlEkoeBOc0K+Xk6IS58eXyxIpLowpug4Tx99SX0nPIj857JQyRu3MI6x0T7Pv3", -- [1]
	"VYzLCsIwEEX/ZdYV0rRak50iSPG1sRs3MtRBC3kRgxJK/93RnXBW9557RwiRXgfvKINWUlRqsSybuSog5UCgYdu1+811vTruoABH7z+1EfKnDpaeCW1gXwpZzgRTn2Wla8VceNk/MGKfKIIewaH9Xp9CyN74e+Y+EhrLWWvMcEMH0/T5", -- [2]
}
"""

COMPRESSED_GOLD_LOG = """
HuokanGoldLog = {
	"nY7NqsIwEIXfZdYVkvQ32SmCFKvd9G6uiIQatJCkIZYrofTd74ggguJCOKuZ78x8uxGcV3+b3qoAgjMSc5pmNC0iGIJTIKCq6wYisOr6DGUFzVOOUGfUZZDGIckIozOCSRrGBM0FyX6x2Z6ll+2gPIgRrDS3o7Vzodf9KeDeK6kNzkqtu6O0ME3Rq9Tj311q9VNWy8Nivl2/UcsJ+6QWi4RjvlPb//8=", -- [1]
}
"""


class ParserTest(unittest.TestCase):
    def setUp(self):
        self._uncompressed_file = self._create_file(UNCOMPRESSED_GOLD_LOG)
        self._compressed_file = self._create_file(COMPRESSED_GOLD_LOG)
        self._empty_log_file = self._create_file(EMPTY_GOLD_LOG)
        self._empty_file = self._create_file("")

    def tearDown(self):
        self._uncompressed_file.close()
        self._compressed_file.close()
        self._empty_log_file.close()
        self._empty_file.close()

    def _create_file(self, text):
        file = tempfile.NamedTemporaryFile("w")
        file.write(text)
        file.flush()
        return file

    def test_parse_uncompressed_log(self):
        log = parse_log_file(self._uncompressed_file.name)
        self.assertListEqual(
            [
                {
                    "character": {"name": "Oppyology", "realm": "Illidan"},
                    "type": "LOOT",
                    "prevMoney": 92039156158,
                    "newMoney": 92039681759,
                    "timestamp": "2021-01-04T22:17:06Z",
                },
                {
                    "character": {"name": "Oppyology", "realm": "Illidan"},
                    "type": "GUILD_BANK",
                    "prevMoney": 92039681759,
                    "newMoney": 92039670259,
                    "timestamp": "2021-01-04T23:49:49Z",
                },
            ],
            log,
        )

    def test_parse_compressed_log(self):
        log = parse_log_file(self._compressed_file.name)
        self.assertListEqual(
            [
                {
                    "character": {"name": "Oppyology", "realm": "Illidan"},
                    "type": "LOOT",
                    "prevMoney": 92039156158,
                    "newMoney": 92039681759,
                    "timestamp": "2021-01-04T22:17:06Z",
                },
                {
                    "character": {"name": "Oppyology", "realm": "Illidan"},
                    "type": "GUILD_BANK",
                    "prevMoney": 92039681759,
                    "newMoney": 92039670259,
                    "timestamp": "2021-01-04T23:49:49Z",
                },
            ],
            log,
        )

    def test_parse_empty_log(self):
        log = parse_log_file(self._empty_log_file.name)
        self.assertListEqual(log, [])

    def test_parse_empty_file(self):
        self.assertRaises(
            ParserException, lambda: parse_log_file(self._empty_file.name)
        )
