import os
import copy
from typing import List

import sys
sys.path.append("util")
from decorators import benchmark
import util

from calculator import Calculator

@benchmark
def part01(expressions: List[str]):
    calc = Calculator()
    results = []
    for expr in expressions:
        results.append(calc.eval(expr))

    return sum(results)


@benchmark
def part02(expressions: List[str]):
    pass


def main(input_file: str = "input.txt"):
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, input_file)

    expressions = []
    with open(input, 'r') as f:
        expressions = [line.strip() for line in f.readlines()]

    print(f"Part01 - Result: {part01(expressions)}")
    #print(f"Part02 - Result: {part02(expressions)}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()