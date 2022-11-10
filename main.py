continue_calc = False


def add(n1, n2):
    return n1 + n2

# subtract


def subtract(n1, n2):
    return n1 - n2


# divide


def divide(n1, n2):
    return n1 / n2

# multiply


def multiply(n1, n2):
    return n1 * n2


operations = {
    '+': add,
    '*': multiply,
    '/': divide,
    '-': subtract
}

number1 = int(input('What is the first number?: '))
for operation in operations:
    print(operation)
operation_symbol = input('Pick an operation from the line above: ')
number2 = int(input('What is the second number?: '))
first_answer = operations[operation_symbol](number1, number2)
print(f'{number1} {operation_symbol} {number2} = {first_answer}')
# operation_symbol = input('Pick another operation: ')
# number3 = int(input('What is the next number?: '))
# second_answer = operations[operation_symbol](first_answer, number3)
# print(f'{first_answer} {operation_symbol} {number3} = {second_answer}')

while not continue_calc:
    response = input(
        f"Enter 'y' if you want to continue with {first_answer}, 'n' if you dont want to ")
    if response == 'y':
        operation_symbol = input('Pick an operation from the line above: ')
        number = int(input('What is the next number?: '))
        second_answer = operations[operation_symbol](first_answer, number)
        # first_answer = second_answer
        print(f'{first_answer} {operation_symbol} {number} = {second_answer}')
    else:
        continue_calc = True
