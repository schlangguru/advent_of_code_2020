import unittest

import day03

class TestDay03(unittest.TestCase):
    def test_part01(self):
        slope = [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"
        ]

        self.assertEqual(day03.part01(slope), 7)

    def test_part02(self):
        slope = [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"
        ]

        self.assertEqual(day03.part02(slope), 336)


if __name__ == '__main__':
    unittest.main()