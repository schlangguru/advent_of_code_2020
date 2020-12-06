import unittest

import day06

class TestDay06(unittest.TestCase):
    def test_part01(self):
        input = """
            abc

            a
            b
            c

            ab
            ac

            a
            a
            a
            a

            b
        """

        self.assertEqual(day06.part01(input), 11)


    def test_part02(self):
        input = """
            abc

            a
            b
            c

            ab
            ac

            a
            a
            a
            a

            b
        """

        self.assertEqual(day06.part02(input), 6)


if __name__ == '__main__':
    unittest.main()