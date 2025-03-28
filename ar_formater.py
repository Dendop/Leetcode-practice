import re

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_numbers = []
    second_numbers = []
    operators = []
    arranged_lines = [[], [], []]  # To store the three lines of the arranged problems
    answers = []

    for problem in problems:
        elements = problem.split()
        if len(elements) != 3:
            return "Error: Invalid problem format."

        first_number, operator, second_number = elements
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        length = max(len(first_number), len(second_number)) + 2

        # Right-align the first number
        top = str(first_number).rjust(length)
        # Right-align the second number, accounting for the operator
        bottom = operator + str(second_number).rjust(length - 1)
        # Create the line of dashes
        line = '-' * length

        arranged_lines[0].append(top)
        arranged_lines[1].append(bottom)
        arranged_lines[2].append(line)

        if show_answers:
            if operator == '+':
                answer = int(first_number) + int(second_number)
            else:
                answer = int(first_number) - int(second_number)
            answers.append(str(answer).rjust(length))

    arranged_string = '\n'.join(['    '.join(line) for line in arranged_lines])

    if show_answers:
        arranged_string += '\n' + '    '.join(answers)

    return arranged_string

def main():
    result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)
    if result:
        print(result)
    
if __name__ == "__main__":
    main()

