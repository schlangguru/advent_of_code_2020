import os
import unittest

import day13

class TestDay13(unittest.TestCase):

    def test_part01(self):
        input = (939, [7,13,59,31,19])
        self.assertEqual(day13.part01(*input), 295)


if __name__ == '__main__':
    unittest.main()