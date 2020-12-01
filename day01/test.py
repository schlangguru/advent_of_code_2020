import unittest

from day01 import findOperands

class TestDay01(unittest.TestCase):
    def test_part01(self):
        data = [1721, 979, 366, 299, 675, 1456]
        result = findOperands(data, 2)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 1721)
        self.assertEqual(result[1], 299)

    def test_part02(self):
        data = [1721, 979, 366, 299, 675, 1456]
        result = findOperands(data, 3)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], 979)
        self.assertEqual(result[1], 366)
        self.assertEqual(result[2], 675)

if __name__ == '__main__':
    unittest.main()