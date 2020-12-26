import pytest

from y2020.day18 import puzzle1, puzzle2


def test_puzzle1_sample():
    answer = puzzle1("../../resources/y2020/day18/day18_1.txt")
    assert 77 == answer


def test_puzzle1_challenge():
    answer = puzzle1("../../resources/y2020/day18/day18_2.txt")
    assert 14006719520523 == answer


def test_puzzle2_sample():
    answer = puzzle2("../../resources/y2020/day18/day18_1.txt")
    assert 97 == answer


def test_puzzle2_challenge():
    answer = puzzle2("../../resources/y2020/day18/day18_2.txt")
    assert 545115449981968 == answer


if __name__ == '__main__':
    pytest.main([__file__])
