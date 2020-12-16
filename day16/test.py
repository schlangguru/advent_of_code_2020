import os
import unittest

import day16
import train_ticket


class TestTicketRule(unittest.TestCase):

    def test_is_valid(self):
        rule = train_ticket.TicketRule("test", (0, 3), (5, 7))

        self.assertEqual(rule.is_valid(0), True)
        self.assertEqual(rule.is_valid(3), True)
        self.assertEqual(rule.is_valid(5), True)
        self.assertEqual(rule.is_valid(7), True)

        self.assertEqual(rule.is_valid(-1), False)
        self.assertEqual(rule.is_valid(4), False)
        self.assertEqual(rule.is_valid(8), False)


class TestTicket(unittest.TestCase):

    def test_invalid_values(self):
        ticket = train_ticket.Ticket(-1, 0, 10, 11)
        rule = train_ticket.TicketRule("test", (0, 10))

        self.assertEqual(ticket.invalid_values(rule), [-1, 11])


class TestDay16(unittest.TestCase):

    def test_part01(self):
        input = """
            class: 1-3 or 5-7
            row: 6-11 or 33-44
            seat: 13-40 or 45-50

            your ticket:
            7,1,14

            nearby tickets:
            7,3,47
            40,4,50
            55,2,20
            38,6,12
        """

        self.assertEqual(day16.part01(*day16.parse_input(input)), 71)


    def test_part02(self):
        pass


if __name__ == '__main__':
    unittest.main()