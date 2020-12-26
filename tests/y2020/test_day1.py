import pathlib

from y2020.day1 import puzzle1, puzzle2


def test_puzzle1_sample():
    assert 514579 == puzzle1(pathlib.Path(__file__).parent.parent.parent / "resources/y2020/day1/day1_1.txt")


def test_puzzle1_challenge():
    assert 1019904 == puzzle1(pathlib.Path(__file__).parent.parent.parent / "resources/y2020/day1/day1_2.txt")


def test_puzzle2_sample():
    assert 241861950 == puzzle2(pathlib.Path(__file__).parent.parent.parent / "resources/y2020/day1/day1_1.txt")


def test_puzzle2_challenge():
    assert 176647680 == puzzle2(pathlib.Path(__file__).parent.parent.parent / "resources/y2020/day1/day1_2.txt")
