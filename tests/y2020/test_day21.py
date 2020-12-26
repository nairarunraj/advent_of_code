import pytest

from y2020.day21 import puzzle1, puzzle2


def test_puzzle1_sample():
    answer = puzzle1("../../resources/y2020/day21/day21_1.txt")
    assert 5 == answer


def test_puzzle1_challenge():
    answer = puzzle1("../../resources/y2020/day21/day21_2.txt")
    assert 2203 == answer


def test_puzzle2_sample():
    answer = puzzle2("../../resources/y2020/day21/day21_1.txt")
    assert 'mxmxvkd,sqjhc,fvjkl' == answer


def test_puzzle2_challenge():
    answer = puzzle2("../../resources/y2020/day21/day21_2.txt")
    assert 'fqfm,kxjttzg,ldm,mnzbc,zjmdst,ndvrq,fkjmz,kjkrm' == answer


if __name__ == '__main__':
    pytest.main([__file__])
