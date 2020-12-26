import unittest

from y2020.day10 import puzzle1, puzzle2


class TestsDay10(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day10/day10_1.txt")
        self.assertEqual(35, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day10/day10_2.txt")
        self.assertEqual(2030, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day10/day10_1.txt")
        self.assertEqual(8, answer)

    def test_puzzle2_sample2(self):
        answer = puzzle2("../../resources/y2020/day10/day10_3.txt")
        self.assertEqual(19208, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day10/day10_2.txt")
        self.assertEqual(42313823813632, answer)


if __name__ == '__main__':
    unittest.main()
