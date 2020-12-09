import unittest

import day09

class TestDay09(unittest.TestCase):
    def test_part01(self):
        data = [
            35,
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576
        ]

        self.assertEqual(day09.part01(data, preamble_length=5), 127)

    def test_part02(self):
        data = [
            35,
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576
        ]

        self.assertEqual(day09.part02(data, preamble_length=5), 62)



if __name__ == '__main__':
    unittest.main()