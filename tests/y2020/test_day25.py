import unittest

from y2020.day25 import puzzle1


class TestsDay25(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day25/day25_1.txt")
        self.assertEqual(14897079, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day25/day25_2.txt")
        self.assertEqual(448851, answer)


if __name__ == '__main__':
    unittest.main()
