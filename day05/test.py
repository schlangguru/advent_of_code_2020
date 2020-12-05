import unittest

import day05

class TestDay05(unittest.TestCase):
    def test_part01(self):
        input = [
            "BFFFBBFRRR",
            "FFFBBBFRRR",
            "BBFFBBFRLL"
        ]

        self.assertEqual(day05.part01(input), 820)


if __name__ == '__main__':
    unittest.main()