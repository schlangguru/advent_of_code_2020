import os
import unittest

import day12
from ship import Ship

class TestDay12(unittest.TestCase):

    def test_part01(self):
        actions = [
            "F10",
            "N3",
            "F7",
            "R90",
            "F11"
        ]

        self.assertEqual(day12.part01(actions),25)


if __name__ == '__main__':
    unittest.main()