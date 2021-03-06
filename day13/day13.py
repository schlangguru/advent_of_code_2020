import os
import copy
import re
import itertools
from typing import List, Tuple, Dict

import sys
sys.path.append("util")
from decorators import benchmark
import util

from bus import Bus

@benchmark
def part01(my_earliest_departure: int, bus_ids: List[int]):
    busses = [Bus(id) for id in map(lambda id: int(id), filter(lambda id: id != 'x', bus_ids))]

    def nearest_departure(bus: Bus) -> int:
        return next(time for time in bus.departure_times() if time >= my_earliest_departure)

    min_departure = sys.maxsize
    bus_id = None
    for bus in busses:
        departure = nearest_departure(bus)
        if departure and departure < min_departure:
            min_departure = departure
            bus_id = bus.id

    return (min_departure - my_earliest_departure) * bus_id


@benchmark
def part02(bus_ids: List[int]):
    offsets = []
    for idx, id in enumerate(bus_ids):
        if id != 'x':
            offsets.append(idx)

    bus_ids = list(map(lambda id: int(id), filter(lambda id: id != 'x', bus_ids)))

    timestamp = 0
    step = 1
    for (bus_id, offset) in zip(bus_ids, offsets):
        while (timestamp + offset) % bus_id != 0:
            timestamp += step
        step *= bus_id

    return timestamp

def main(input_file: str = "input.txt"):
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, input_file)

    lines = []
    with open(input, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    my_earliest_departure = int(lines[0])
    bus_ids = lines[1].split(',')

    print(f"Part01 - Result {part01(my_earliest_departure, copy.deepcopy(bus_ids))}")
    print(f"Part02 - Result {part02(copy.deepcopy(bus_ids))}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()