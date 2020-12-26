import unittest

from y2020.day7 import puzzle1, puzzle2


class TestsDay7(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day7/day7_1.txt")
        self.assertEqual(4, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day7/day7_2.txt")
        self.assertEqual(248, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day7/day7_3.txt")
        self.assertEqual(126, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day7/day7_2.txt")
        self.assertEqual(57281, answer)


if __name__ == '__main__':
    unittest.main()
