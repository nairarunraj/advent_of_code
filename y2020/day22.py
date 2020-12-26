"""
--- Day 22: Crab Combat ---
"""
import copy

from y2020.file_utils import get_input_data


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)

    player = player1 = []
    for line in input_content:
        if 'Player' in line:
            continue

        if line == '':
            player1 = copy.deepcopy(player)
            player = []
            continue

        player.append(int(line))

    player2 = player

    while len(player1) != 0 and len(player2) != 0:
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)

    if len(player1) == 0:
        player = player2
    else:
        player = player1

    return sum([i * card for i, card in enumerate(reversed(player), 1)])


def play_game(player1, player2):
    dealt_cards = set()
    while len(player1) != 0 and len(player2) != 0:
        if (tuple(player1), tuple(player2)) in dealt_cards:
            return 1

        dealt_cards.add((tuple(player1), tuple(player2)))

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if card1 <= len(player1) and card2 <= len(player2):
            winner = play_game(player1[:card1], player2[:card2])
            if winner == 1:
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)
        elif card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)

    if len(player1) == 0:
        return 2
    else:
        return 1


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    player = player1 = []
    for line in input_content:
        if 'Player' in line:
            continue

        if line == '':
            player1 = copy.deepcopy(player)
            player = []
            continue

        player.append(int(line))

    player2 = player

    winner = play_game(player1, player2)

    if winner == 1:
        player = player1
    else:
        player = player2

    return sum([i * card for i, card in enumerate(reversed(player), 1)])


if __name__ == '__main__':
    answer = puzzle1("../resources/y2020/day22/day22_1.txt")
    print(answer)

    answer = puzzle1("../resources/y2020/day22/day22_2.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day22/day22_1.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day22/day22_2.txt")
    print(answer)
