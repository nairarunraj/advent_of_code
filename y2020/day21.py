"""
--- Day 21: Allergen Assessment ---
"""
from collections import defaultdict

from y2020.file_utils import get_input_data


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)

    foods = []
    for line in input_content:
        (ingredients, allergens) = line.split(' (contains ')
        ing = set(ingredients.split(' '))

        aller = set(allergens[:-1].split(', '))
        foods.append((ing, aller))

    all_ing = set()
    all_allerg = set()
    for ing, aller in foods:
        all_ing |= ing
        all_allerg |= aller

    possible_allergic_ing = {ing: set(all_allerg) for ing in all_ing}

    count_ings = defaultdict(int)
    for ings, allergs in foods:
        for ing in ings:
            count_ings[ing] += 1

        for allerg in allergs:
            for ing in all_ing:
                if ing not in ings:
                    possible_allergic_ing[ing].discard(allerg)

    count = 0
    for ing in all_ing:
        if not possible_allergic_ing[ing]:
            count += count_ings[ing]

    return count


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    foods = []
    for line in input_content:
        (ingredients, allergens) = line.split(' (contains ')
        ing = set(ingredients.split(' '))

        aller = set(allergens[:-1].split(', '))
        foods.append((ing, aller))

    all_ing = set()
    all_allerg = set()
    for ing, aller in foods:
        all_ing |= ing
        all_allerg |= aller

    possible_allergic_ing = {ing: set(all_allerg) for ing in all_ing}

    for ings, allergs in foods:
        for allerg in allergs:
            for ing in all_ing:
                if ing not in ings:
                    possible_allergic_ing[ing].discard(allerg)

    fixed_allergic_ing = {}
    while len(fixed_allergic_ing) < len(all_allerg):
        new_possible_allergic_ing = possible_allergic_ing
        for ing, allergs in possible_allergic_ing.items():
            if len(allergs) == 1:
                for allerg in allergs:
                    fixed_allergic_ing[allerg] = ing

                continue

            new_allergs = set()
            for allerg in allergs:
                if allerg not in fixed_allergic_ing:
                    new_allergs.add(allerg)

            new_possible_allergic_ing[ing] = new_allergs

        possible_allergic_ing = new_possible_allergic_ing

    ing_list = [fixed_allergic_ing[allerg] for allerg in sorted(fixed_allergic_ing)]

    return ','.join(ing_list)


if __name__ == '__main__':
    answer = puzzle1("../resources/y2020/day21/day21_1.txt")
    print(answer)

    answer = puzzle1("../resources/y2020/day21/day21_2.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day21/day21_1.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day21/day21_2.txt")
    print(answer)
