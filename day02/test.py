import unittest

import day02

class TestDay02(unittest.TestCase):
    def test_part01(self):
        lines = [
            "1-3 a: abcde",
            "1-3 b: cdefg",
            "2-9 c: ccccccccc"
        ]

        self.assertEqual(day02.part01(lines), 2)

    def test_part02(self):
        lines = [
            "1-3 a: abcde",
            "1-3 b: cdefg",
            "2-9 c: ccccccccc"
        ]

        self.assertEqual(day02.part02(lines), 1)


if __name__ == '__main__':
    unittest.main()