import pytest

from y2020.day17 import puzzle1, puzzle2


def test_puzzle1_sample():
    answer = puzzle1("../../resources/y2020/day17/day17_1.txt")
    assert 112 == answer


def test_puzzle1_challenge():
    answer = puzzle1("../../resources/y2020/day17/day17_2.txt")
    assert 336 == answer


def test_puzzle2_sample():
    answer = puzzle2("../../resources/y2020/day17/day17_1.txt")
    assert 848 == answer


def test_puzzle2_challenge():
    answer = puzzle2("../../resources/y2020/day17/day17_2.txt")
    assert 2620 == answer


if __name__ == '__main__':
    pytest.main([__file__])
