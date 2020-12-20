import os
import unittest

import day19

class TestDay19(unittest.TestCase):

    def test_part01(self):
        # input = """
        #     0: 1 2
        #     1: "a"
        #     2: 1 3 | 3 1
        #     3: "b"

        #     aab
        #     aba
        #     aaa
        # """

        # self.assertEqual(day19.part01(input), 2)

        input = """
            0: 4 1 5
            1: 2 3 | 3 2
            2: 4 4 | 5 5
            3: 4 5 | 5 4
            4: "a"
            5: "b"

            ababbb
            bababa
            abbbab
            aaabbb
            aaaabbb
        """

        self.assertEqual(day19.part01(input), 2)


    def test_part02(self):
        pass


if __name__ == '__main__':
    unittest.main()