import os
import unittest

import day20

class TestDay19(unittest.TestCase):

    def test_part01(self):
        tile_input = read("input.test.txt")
        self.assertEqual(day20.part01(tile_input), 20899048083289)


def read(input: str):
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, input)

    content = ""
    with open(input, 'r') as f:
        content = f.read()

    return content


if __name__ == '__main__':
    unittest.main()