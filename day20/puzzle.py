from typing import List


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
        if direction == 't':
            return self.tile[0]
        elif direction == 'b':
            return self.tile[len(self.tile) - 1]
        elif direction == 'r':
            return "".join(list(zip(*self.tile))[len(self.tile) - 1])
        elif direction == 'l':
            return "".join(list(zip(*self.tile))[0])
        else:
            raise Exception(f"Direction {direction} not valid")


    def borders(self) -> List[str]:
        return [self.border(direction) for direction in ['t', 'r', 'b', 'l']]


    def __repr__(self):
        tile = '\n'.join(self.tile)

        return f"Tile {self.id}:\n{tile}"


def parse_tiles(input: str) -> List[Tile]:
    return list(map(Tile.parse, input.strip().split("\n\n")))


def find_corner_tiles(tiles: List[Tile]) -> List[Tile]:
    corner = []
    for tile in tiles:
        if is_corner_tile(tile, tiles):
            corner.append(tile)

    return corner


def is_corner_tile(tile: Tile, tiles: List[Tile]) -> bool:
    others = [other for other in tiles if other != tile]
    shared_border_count = 0
    for border in tile.borders():
        if border in all_borders(others):
            shared_border_count += 1

    return shared_border_count == 2


def all_borders(tiles: List[Tile]):
    for tile in tiles:
        for variation in tile.variations():
            for border in variation.borders():
                yield border
