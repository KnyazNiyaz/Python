operation = input(
    "'Please type in the math operation you would like to complete\n"
    "+ for addition"
    "- for subtraction"
    "* for multiplication"
    "/ for division'"
)

num_1 = int(input('Enter first num: '))
print()
num_2 = int(input('Enter second num: '))

if operation == '+':
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)
elif operation == '-':
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)
elif operation == '*':
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)
elif operation == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)
else:
    print('YOu have typed a valid operator')