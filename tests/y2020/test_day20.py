import pytest

from y2020.day20 import puzzle1, puzzle2


def test_puzzle1_sample():
    answer = puzzle1("../../resources/y2020/day20/day20_1.txt")
    assert 20899048083289 == answer


def test_puzzle1_challenge():
    answer = puzzle1("../../resources/y2020/day20/day20_2.txt")
    assert 59187348943703 == answer


def test_puzzle2_sample2():
    answer = puzzle2("../../resources/y2020/day20/day20_1.txt")
    assert 273 == answer


def test_puzzle2_challenge():
    answer = puzzle2("../../resources/y2020/day20/day20_2.txt")
    assert 1565 == answer


if __name__ == '__main__':
    pytest.main([__file__])
