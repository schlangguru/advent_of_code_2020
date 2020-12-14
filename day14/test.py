import os
import unittest

from emulation import Bitmask

class TestDay12(unittest.TestCase):

    def test_bitmask(self):
        mask = Bitmask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        self.assertEqual(mask.apply(11), 73)

        mask = Bitmask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        self.assertEqual(mask.apply(101), 101)

        mask = Bitmask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        self.assertEqual(mask.apply(0), 64)


if __name__ == '__main__':
    unittest.main()