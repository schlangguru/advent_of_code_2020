import unittest

import day10

class TestDay10(unittest.TestCase):
    def test_part01_1(self):
        data = [
            16,
            10,
            15,
            5,
            1,
            11,
            7,
            19,
            6,
            12,
            4
        ]
        expected_jolt_distribution = {
            1: 7,
            3: 5
        }

        self.assertEqual(day10.part01(data), expected_jolt_distribution)

    def test_part01_2(self):
        data = [
            28,
            33,
            18,
            42,
            31,
            14,
            46,
            20,
            48,
            47,
            24,
            23,
            49,
            45,
            19,
            38,
            39,
            11,
            1,
            32,
            25,
            35,
            8,
            17,
            7,
            9,
            4,
            2,
            34,
            10,
            3
        ]
        expected_jolt_distribution = {
            1: 22,
            3: 10
        }

        self.assertEqual(day10.part01(data), expected_jolt_distribution)


    def test_part02_1(self):
        data = [
            16,
            10,
            15,
            5,
            1,
            11,
            7,
            19,
            6,
            12,
            4
        ]

        self.assertEqual(day10.part02(data), 8)


    def test_part02_2(self):
        data = [
            28,
            33,
            18,
            42,
            31,
            14,
            46,
            20,
            48,
            47,
            24,
            23,
            49,
            45,
            19,
            38,
            39,
            11,
            1,
            32,
            25,
            35,
            8,
            17,
            7,
            9,
            4,
            2,
            34,
            10,
            3
        ]

        self.assertEqual(day10.part02(data), 19208)

if __name__ == '__main__':
    unittest.main()