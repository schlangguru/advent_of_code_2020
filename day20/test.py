import os
import unittest

import puzzle
import day20

class TestTile(unittest.TestCase):

    def test_border(self):
        tile =  puzzle.Tile("id", [
            "123",
            "456",
            "789"
        ])

        self.assertEqual(tile.borders(), ["123", "369", "987", "741"])


    def test_rotation(self):
        tile =  puzzle.Tile("id", [
            "123",
            "456",
            "789"
        ])

        rotations = {
            0: [
                "123",
                "456",
                "789"
            ],
            90: [
                "741",
                "852",
                "963"
            ],
            180: [
                "987",
                "654",
                "321"
            ],
            270: [
                "369",
                "258",
                "147"
            ]
        }

        self.assertEqual([tile.rotated(degree).tile for degree in rotations.keys()], list(rotations.values()))


    def test_flip(self):
        tile =  puzzle.Tile("id", [
            "123",
            "456",
            "789"
        ])

        flipped_rotations = {
            0: [
                "789",
                "456",
                "123"
            ],
            90: [
                "147",
                "258",
                "369"
            ],
            180: [
                "321",
                "654",
                "987"
            ],
            270: [
                "963",
                "852",
                "741"
            ]
        }

        self.assertEqual([tile.flipped().rotated(degree).tile for degree in flipped_rotations.keys()], list(flipped_rotations.values()))


    def test_match_rotated(self):
        tile =  puzzle.Tile("0", [
            "...",
            "..#",
            "..."
        ])
        other =  puzzle.Tile("1", [
            ".x.",
            "x.x",
            ".#."
        ])

        match_direction, matched_tile = tile.match(other)
        self.assertEqual(match_direction, puzzle.Direction.EAST)
        self.assertEqual(matched_tile.tile, other.rotated(90).tile)


    def test_match_flipped(self):
        tile =  puzzle.Tile("0", [
            "y.y",
            "y.y",
            "#.."
        ])
        other =  puzzle.Tile("1", [
            "x.x",
            "x.x",
            "#.."
        ])

        match_direction, matched_tile = tile.match(other)
        self.assertEqual(match_direction, puzzle.Direction.SOUTH)
        self.assertEqual(matched_tile.tile, other.flipped().tile)


    def test_delete_border(self):
        tile =  puzzle.Tile("0", [
            "###",
            "#.#",
            "###"
        ])

        tile.delete_border()
        self.assertEqual(tile.tile, ["."])

class TestDay19(unittest.TestCase):

    def test_part01(self):
        tile_input = read("input.test.txt")
        self.assertEqual(day20.part01(tile_input), 20899048083289)


    def test_part02(self):
        tile_input = read("input.test.txt")
        self.assertEqual(day20.part02(tile_input), 273)


def read(input: str):
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, input)

    content = ""
    with open(input, 'r') as f:
        content = f.read()

    return content


if __name__ == '__main__':
    unittest.main()