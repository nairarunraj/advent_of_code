import pytest

from y2020.day22 import puzzle1, puzzle2


def test_puzzle1_sample():
    answer = puzzle1("../../resources/y2020/day22/day22_1.txt")
    assert 306 == answer


def test_puzzle1_challenge():
    answer = puzzle1("../../resources/y2020/day22/day22_2.txt")
    assert 30780 == answer


def test_puzzle2_sample():
    answer = puzzle2("../../resources/y2020/day22/day22_1.txt")
    assert 291 == answer


def test_puzzle2_challenge():
    answer = puzzle2("../../resources/y2020/day22/day22_2.txt")
    assert 36621 == answer


if __name__ == '__main__':
    pytest.main([__file__])
