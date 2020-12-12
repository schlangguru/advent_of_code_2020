import os
import copy
from typing import List, Tuple, Dict

import sys
sys.path.append("util")
from decorators import benchmark
import util

from simulation import SeatPlan, SeatPlanSimulator, OCCUPIED_SEAT

@benchmark
def part01(seats: List[List[chr]]):
    simulator = SeatPlanSimulator(SeatPlan(seats), rule_set="part01")
    applied_updates = simulator.simulate_round()
    while len(applied_updates) > 0:
        applied_updates = simulator.simulate_round()

    return simulator.seat_plan.count(OCCUPIED_SEAT)


@benchmark
def part02(seats: List[List[chr]]):
    simulator = SeatPlanSimulator(SeatPlan(seats), rule_set="part02")
    applied_updates = simulator.simulate_round()
    while len(applied_updates) > 0:
        applied_updates = simulator.simulate_round()

    return simulator.seat_plan.count(OCCUPIED_SEAT)


def main(input_file: str = "input.txt"):
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, input_file)

    seats = []
    with open(input, 'r') as f:
        seats = [list(line.strip()) for line in f.readlines()]

    print(f"Part01 - Number of occupied seats {part01(copy.deepcopy(seats))}")
    print(f"Part02 - Number of occupied seats {part02(copy.deepcopy(seats))}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()