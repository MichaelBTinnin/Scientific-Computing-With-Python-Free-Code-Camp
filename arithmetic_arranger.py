def arithmetic_arranger(problems, answer=False):
    # Determine there aren't too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Parts of the problems
    operand_1 = []
    operand_2 = []
    operator = []

    # Lines to display
    line_1 = []
    line_2 = []
    line_3 = []
    line_4 = []

    for problem in problems:
        problem_parts = problem.split()
        operand_1.append(problem_parts[0])
        operator.append(problem_parts[1])
        operand_2.append(problem_parts[2])

    for i in operator:
        if '*' in i or '/' in i:
            return "Error: Operator must be '+' or '-'."

    for i in range(len(operand_1)):
        if not operand_1[i].isdigit() or not operand_2[i].isdigit():
            return "Error: Numbers must only contain digits."

    for i in range(len(operand_1)):
        if len(operand_1[i]) > 4 or len(operand_2[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    i = 0
    while i < len(operand_1):
        if len(operand_1[i]) > len(operand_2[i]):
            line_1.append("  " + operand_1[i])
            spaces = " " * (len(operand_1[i]) - len(operand_2[i]) + 1)
            line_2.append(operator[i] + spaces + operand_2[i])
            line_3.append('-' * (len(operand_1[i]) + 2))
        else:
            spaces = " " * (len(operand_2[i]) - len(operand_1[i]) + 2)
            line_1.append(spaces + operand_1[i])
            line_2.append(operator[i] + " " + operand_2[i])
            line_3.append('-' * (len(operand_2[i]) + 2))
        i += 1

    arranged_problems = ''
    if answer:
        for i in range(len(operand_1)):
            if operator[i] == '+':
                result = str(int(operand_1[i]) + int(operand_2[i]))
            else:
                result = str(int(operand_1[i]) - int(operand_2[i]))

            if len(result) > max(len(operand_1[i]), len(operand_2[i])):
                line_4.append(" " + result)
            else:
                line_4.append("  " + result)

        for i in range(len(operand_1)):
            arranged_problems += line_1[i]
            if i < len(operand_1) - 1:
                arranged_problems += "    "
        arranged_problems += "\n"
        for i in range(len(operand_1)):
            arranged_problems += line_2[i]
            if i < len(operand_1) - 1:
                arranged_problems += "    "
        arranged_problems += "\n"
        for i in range(len(operand_1)):
            arranged_problems += line_3[i]
            if i < len(operand_1) - 1:
                arranged_problems += "    "
        arranged_problems += "\n"
        for i in range(len(operand_1)):
            arranged_problems += line_4[i]
            if i < len(operand_1) - 1:
                arranged_problems += "    "

    else:
        for i in range(len(operand_1)):
            arranged_problems += line_1[i]
            if i < len(operand_1) - 1:
                arranged_problems += "    "
        arranged_problems += "\n"
        for i in range(len(operand_1)):
            arranged_problems += line_2[i]
            if i < len(operand_1) - 1:
                arranged_problems += "    "
        arranged_problems += "\n"
        for i in range(len(operand_1)):
            arranged_problems += line_3[i]
            if i < len(operand_1) - 1:
                arranged_problems += "    "

    return arranged_problems
