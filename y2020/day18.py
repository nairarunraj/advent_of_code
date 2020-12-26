"""
--- Day 18: Operation Order ---
"""

from y2020.file_utils import get_input_data


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)

    sum_expr = 0
    for line in input_content:
        line = line.replace("(", " ( ")
        line = line.replace(")", " ) ")
        exprs = line.split(' ')
        operands = []
        operators = []
        for expr in exprs:
            if expr == '':
                continue
            if expr in ('+', '*'):
                if len(operators) > 0 and operators[-1] in ('+', '*'):
                    operator = operators.pop()
                    operand1 = operands.pop()
                    operand2 = operands.pop()
                    if operator == '+':
                        operands.append(operand1 + operand2)
                    if operator == '*':
                        operands.append(operand1 * operand2)
                operators.append(expr)
                continue

            if expr == '(':
                operators.append('(')
                continue

            if expr == ')':
                while (operator := operators.pop()) != '(':
                    operand1 = operands.pop()
                    operand2 = operands.pop()
                    if operator == '+':
                        operands.append(operand1 + operand2)
                    if operator == '*':
                        operands.append(operand1 * operand2)

                continue

            operands.append(int(expr))

        while len(operators) > 0 and (operator := operators.pop()) != '(':
            operand1 = operands.pop()
            operand2 = operands.pop()
            if operator == '+':
                operands.append(operand1 + operand2)
            if operator == '*':
                operands.append(operand1 * operand2)

        sum_expr += operands[0]

    return sum_expr


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    sum_expr = 0
    for line in input_content:
        line = line.replace("(", " ( ")
        line = line.replace(")", " ) ")
        exprs = line.split(' ')
        operands = []
        operators = []
        for expr in exprs:
            if expr == '':
                continue
            if expr == '+':
                if len(operators) > 0 and operators[-1] == '+':
                    operator = operators.pop()
                    operand1 = operands.pop()
                    operand2 = operands.pop()
                    if operator == '+':
                        operands.append(operand1 + operand2)
                    if operator == '*':
                        operands.append(operand1 * operand2)
                operators.append(expr)
                continue

            if expr == '*':
                if len(operators) > 0 and operators[-1] in ('+', '*'):
                    operator = operators.pop()
                    operand1 = operands.pop()
                    operand2 = operands.pop()
                    if operator == '+':
                        operands.append(operand1 + operand2)
                    if operator == '*':
                        operands.append(operand1 * operand2)
                operators.append(expr)
                continue

            if expr == '(':
                operators.append('(')
                continue

            if expr == ')':
                while (operator := operators.pop()) != '(':
                    operand1 = operands.pop()
                    operand2 = operands.pop()
                    if operator == '+':
                        operands.append(operand1 + operand2)
                    if operator == '*':
                        operands.append(operand1 * operand2)

                continue

            operands.append(int(expr))

        while len(operators) > 0 and (operator := operators.pop()) != '(':
            operand1 = operands.pop()
            operand2 = operands.pop()
            if operator == '+':
                operands.append(operand1 + operand2)
            if operator == '*':
                operands.append(operand1 * operand2)

        sum_expr += operands[0]

    return sum_expr


if __name__ == '__main__':
    answer = puzzle1("../resources/y2020/day18/day18_1.txt")
    print(answer)

    answer = puzzle1("../resources/y2020/day18/day18_2.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day18/day18_1.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day18/day18_2.txt")
    print(answer)
