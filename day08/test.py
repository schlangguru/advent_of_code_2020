import unittest

import day08

class TestDay08(unittest.TestCase):
    def test_part01(self):
        instructions = [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6"
        ]

        self.assertEqual(day08.part01(instructions)["accumulator"], 5)

    def test_part02(self):
        instructions = [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6"
        ]

        self.assertEqual(day08.part02(instructions)["accumulator"], 8)


if __name__ == '__main__':
    unittest.main()