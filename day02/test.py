import unittest

import day02

class TestDay01(unittest.TestCase):
    def test_part01(self):
        lines = [
            "1-3 a: abcde",
            "1-3 b: cdefg",
            "2-9 c: ccccccccc"
        ]

        self.assertEqual(day02.get_number_of_valid_passwords(lines), 2)


if __name__ == '__main__':
    unittest.main()