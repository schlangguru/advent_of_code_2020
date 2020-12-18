import os
import unittest

import day18

class TestDay18(unittest.TestCase):

    def test_part01(self):
        self.assertEqual(day18.part01(["2 * 3 + (4 * 5)"]), 26)
        self.assertEqual(day18.part01(["5 + (8 * 3 + 9 + 3 * 4 * 3)"]), 437)
        self.assertEqual(day18.part01(["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"]), 12240)
        self.assertEqual(day18.part01(["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]), 13632)


    def test_part02(self):
        pass


if __name__ == '__main__':
    unittest.main()