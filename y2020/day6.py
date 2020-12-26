"""
--- Day 6: Custom Customs ---
"""

from y2020.file_utils import get_input_data_newline_separated


def puzzle1(input_file) -> int:
    input_content = get_input_data_newline_separated(input_file)
    sum_questions = 0
    for answer_group in input_content:
        questions_answered = {}
        for ans_person in answer_group:
            for question in ans_person:
                questions_answered[question] = 1

        sum_questions += len(questions_answered.keys())

    return sum_questions


def puzzle2(input_file) -> int:
    input_content = get_input_data_newline_separated(input_file)

    sum_questions = 0
    for answer_group in input_content:
        questions_answered = {}

        for ans_person in answer_group:
            for question in ans_person:
                if question in questions_answered:
                    questions_answered[question] += 1
                else:
                    questions_answered[question] = 1

        persons_in_group = len(answer_group)
        for question, no_of_people_who_answered in questions_answered.items():
            if no_of_people_who_answered == persons_in_group:
                sum_questions += 1

    return sum_questions


if __name__ == '__main__':
    answer = puzzle1("../../resources/y2020/day6/day6_1.txt")
    print(answer)

    answer = puzzle1("../../resources/y2020/day6/day6_2.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day6/day6_1.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day6/day6_2.txt")
    print(answer)
