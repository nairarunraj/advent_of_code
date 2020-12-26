import pytest

from y2020.day19 import puzzle1, puzzle2


def test_puzzle1_sample():
    answer = puzzle1("../../resources/y2020/day19/day19_1.txt")
    assert 2 == answer


def test_puzzle1_challenge():
    answer = puzzle1("../../resources/y2020/day19/day19_2.txt")
    assert 136 == answer


def test_puzzle2_sample():
    answer = puzzle2("../../resources/y2020/day19/day19_1.txt")
    assert 2 == answer


def test_puzzle2_sample2():
    answer = puzzle2("../../resources/y2020/day19/day19_3.txt")
    assert 12 == answer


def test_puzzle2_challenge():
    answer = puzzle2("../../resources/y2020/day19/day19_2.txt")
    assert 256 == answer


if __name__ == '__main__':
    pytest.main([__file__])
