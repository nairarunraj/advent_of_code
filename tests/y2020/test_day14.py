import unittest

from y2020.day14 import puzzle1, puzzle2


class TestsDay14(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day14/day14_1.txt")
        self.assertEqual(165, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day14/day14_2.txt")
        self.assertEqual(6386593869035, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day14/day14_3.txt")
        self.assertEqual(208, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day14/day14_2.txt")
        self.assertEqual(4288986482164, answer)


if __name__ == '__main__':
    unittest.main()
