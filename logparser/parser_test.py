import unittest
import tempfile
import os
from .parser import parse_log_file

uncompressed_gold_log = """
HuokanGoldLog = {
	"TczNCsIwEATgd9lzhSSatMkbCEouPXlb6qKF/BGDEkrf3fUmzGnm292gVHpfc6IOzipxtFIbqacBWi8EDi7ezzBAos8/MpMctWW0Rno1jIWlEkoeBOc0K+Xk6IS58eXyxIpLowpug4Tx99SX0nPIj857JQyRu3MI6x0T7Pv3", -- [1]
	"VYzLCsIwEEX/ZdYV0rRak50iSPG1sRs3MtRBC3kRgxJK/93RnXBW9557RwiRXgfvKINWUlRqsSybuSog5UCgYdu1+811vTruoABH7z+1EfKnDpaeCW1gXwpZzgRTn2Wla8VceNk/MGKfKIIewaH9Xp9CyN74e+Y+EhrLWWvMcEMH0/T5", -- [2]
}
"""


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.file = tempfile.NamedTemporaryFile("w")
        self.file.write(uncompressed_gold_log)
        self.file.flush()

    def tearDown(self):
        self.file.close()

    def testParseUncompressedLog(self):
        log = parse_log_file(self.file.name)
        self.assertDictEqual(
            {
                "character": {"name": "Oppyology", "realm": "Illidan"},
                "type": "LOOT",
                "prevMoney": 92039156158,
                "newMoney": 92039681759,
                "timestamp": "2021-01-04T22:17:06Z",
            },
            log[0],
        )
        self.assertDictEqual(
            {
                "character": {"name": "Oppyology", "realm": "Illidan"},
                "type": "GUILD_BANK",
                "prevMoney": 92039681759,
                "newMoney": 92039670259,
                "timestamp": "2021-01-04T23:49:49Z",
            },
            log[1],
        )

    def testParseMixedCompressionLog(self):
        pass
