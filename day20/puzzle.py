from typing import List, Tuple
from enum import Enum
import re

class Direction(Enum):
    NORTH = "n"
    EAST = "e"
    SOUTH = "s"
    WEST = "w"

    @staticmethod
    def counter_direction(direction: "Direction"):
        if direction == Direction.NORTH:
            return Direction.SOUTH
        elif direction == Direction.EAST:
            return Direction.WEST
        elif direction == Direction.SOUTH:
            return Direction.NORTH
        elif direction == Direction.WEST:
            return Direction.EAST
        else:
            raise Exception(f"Invalid direction '{direction}'")


class Tile():

    def __init__(self, id: str, tile: List[str]):
        self.id = id
        self.tile = tile


    @classmethod
    def parse(cls, tile_str: str) -> "Tile":
        [id, *tile] = [line.strip() for line in tile_str.split('\n')]
        id = id[5:-1]

        return cls(id, tile)


    def flipped(self) -> "Tile":
        return Tile(self.id, list(reversed(self.tile)))


    def rotated(self, degree: int) -> "Tile":
        tile = self.tile
        for _ in range(int(degree / 90)):
            tile = ["".join(list(reversed(cols))) for cols in zip(*tile)]

        return Tile(self.id, tile)


    def variations(self) -> List["Tile"]:
        variations = [self.rotated(deg) for deg in [0, 90, 180, 270]]
        variations += [self.flipped().rotated(deg) for deg in [0, 90, 180, 270]]

        return variations


    def border(self, direction: str) -> str:
        if direction == Direction.NORTH:
            return self.tile[0]
        elif direction == Direction.SOUTH:
            return self.tile[len(self.tile) - 1][::-1]
        elif direction == Direction.EAST:
            return "".join(list(zip(*self.tile))[len(self.tile) - 1])
        elif direction == Direction.WEST:
            return "".join(list(zip(*self.tile))[0])[::-1]
        else:
            raise Exception(f"Direction {direction} not valid")


    def borders(self) -> List[str]:
        return [self.border(direction) for direction in Direction]


    def flipped_borders(self) -> List[str]:
        return [self.border(direction)[::-1] for direction in Direction]


    def match(self, other: "Tile") -> Tuple[Direction, "Tile"]:
        for direction in Direction:
            if match := self.match_direction(other, direction):
                return (direction, match)

        return None


    def match_direction(self, other: "Tile", direction: Direction) -> "Tile":
        my_border = "".join(reversed(self.border(direction))) # Since we match in counter-direction we need to reverse the border
        if match := self.match_border(my_border, direction, other):
            return match

        return None


    def match_border(self, my_border: str, match_direction: Direction, other: "Tile") -> "Tile":
        counter_direction = Direction.counter_direction(match_direction)
        if my_border in other.borders():
            other_borders = other.borders()
            for variation in [other.rotated(deg) for deg in [0, 90, 180, 270]]:
                if my_border == variation.border(counter_direction):
                    return variation
        elif my_border in other.flipped_borders():
            flip = other.flipped()
            for variation in [flip.rotated(deg) for deg in [0, 90, 180, 270]]:
                if my_border == variation.border(counter_direction):
                    return variation
        else:
            return None


    def delete_border(self):
        self.tile.pop(0)
        self.tile.pop()
        self.tile = list(map(lambda line: line[1:-1], self.tile))


    def __repr__(self):
        tile = '\n'.join(self.tile)

        return f"Tile {self.id}:\n{tile}"


class Puzzle():

    def __init__(self):
        self.tiles = {}


    def set_tile(self, position: Tuple[int, int], tile: Tile):
        self.tiles[position] = tile


    def as_tile(self):
        value = []
        xs, ys = zip(*self.tiles.keys())
        for y in range(min(ys), max(ys) + 1):
            lines = [""]*len(self.tiles[(0,0)].tile)
            for x in range(min(xs), max(xs) + 1):
                tile = self.tiles[(x, y)]
                for i, line in enumerate(tile.tile):
                    lines[i] = lines[i] + line
            value.extend(lines)

        return Tile("Puzzle", value)


    def __repr__(self):
        grid = []
        xs, ys = zip(*self.tiles.keys())
        for y in range(min(ys), max(ys) + 1):
            cols = []
            for x in range(min(xs), max(xs) + 1):
                tile = self.tiles[(x, y)]
                cols.append(tile.id)
            line = " | ".join(cols)
            grid.append(line)

        return "\n".join(grid)


def parse_tiles(input: str) -> List[Tile]:
    return list(map(Tile.parse, input.strip().split("\n\n")))


def find_corner_tiles(tiles: List[Tile]) -> List[Tile]:
    corners = []
    for tile in tiles:
        if is_corner_tile(tile, tiles):
            corners.append(tile)

    return corners


def is_corner_tile(tile: Tile, tiles: List[Tile]) -> bool:
    others = [other for other in tiles if other.id != tile.id]
    shared_border_count = 0
    for border in tile.borders():
        if border in all_borders(others):
            shared_border_count += 1

    return shared_border_count <= 2


def all_borders(tiles: List[Tile]):
    for tile in tiles:
        for border in [*tile.borders(), *tile.flipped_borders()]:
            yield border


def find_north_west_corner(corners: List[Tile], others: List[Tile]):
    for corner in corners:
        for variation in [corner.rotated(deg) for deg in [0, 90, 180, 270]]:
            directions = []
            for other in others:
                if match := variation.match(other):
                    match_direction = match[0]
                    directions.append(match_direction)
            if Direction.EAST in directions and Direction.SOUTH in directions:
                return variation


def find_match(tile: Tile, others: List[Tile], direction: Direction) -> Tile:
    for other in others:
        if match := tile.match_direction(other, direction):
            return match

    return None


def count_monster(image: List[str]) -> int:
    monster_top = pattern = re.compile(r".{18}\#")
    monster_mid = pattern = re.compile(r"\#....\#\#....\##....\#\#\#")
    monster_btm = pattern = re.compile(r".\#..\#..\#..\#..\#..\#")

    count = 0
    for i, line in enumerate(image):
        # since we search the monter mid first
        # we need to skip first and last line
        if i == 0 or i == (len(image) - 1):
            continue

        match_idx = -1
        while match := monster_mid.search(line, match_idx+1):
            match_idx = match.start()
            if monster_top.match(image[i-1], match_idx) and monster_btm.match(image[i+1], match_idx):
                count += 1

    return count


def build_puzzle(tiles: List[Tile]):
    puzzle = Puzzle()
    start = find_north_west_corner(find_corner_tiles(tiles), tiles)
    others = [other for other in tiles if other.id != start.id]

    pos = (0, 0)
    puzzle.set_tile(pos, start)

    # Go down in first direction
    while match := find_match(start, others, Direction.SOUTH):
        pos = (pos[0], pos[1] + 1)
        puzzle.set_tile(pos, match)
        start = match
        others = list(filter(lambda t: t.id != match.id, others))

    # for each tile in the first line match diagonal lines
    for pos, tile in puzzle.tiles.copy().items():
        while match := find_match(tile, others, Direction.EAST):
            pos = (pos[0] + 1, pos[1])
            puzzle.set_tile(pos, match)
            tile = match
            others = list(filter(lambda t: t.id != match.id, others))


    # Delete borders
    for _, tile in puzzle.tiles.items():
        tile.delete_border()

    return puzzle
