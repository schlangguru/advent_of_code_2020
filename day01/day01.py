import os
import itertools

def findOperands(expenses, numberOfOperands):
    """
    Finds 'numberOfOperands' in 'expenses' that sum to 2020.
    """
    combinations = itertools.combinations(expenses, numberOfOperands)
    operands = list(filter(lambda l: sum(l) == 2020, combinations))
    return operands[0]

def part01(expenses):
    """
    Part 01: Find 2 Operands that sum to 2020
    """
    operands = findOperands(expenses, 2)
    return operands[0] * operands[1]

def part02(expenses):
    """
    Part 01: Find 3 Operands that sum to 2020
    """
    operands = findOperands(expenses, 3)
    return operands[0] * operands[1] * operands[2]

def main():
    working_dir = os.path.dirname(__file__)
    input_file = os.path.join(working_dir, 'input.txt')

    expenses = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
        expenses = [int(x.strip()) for x in lines]

    print ("Part 01:", part01(expenses))
    print ("Part 02:", part02(expenses))

if __name__ == '__main__':
    main()