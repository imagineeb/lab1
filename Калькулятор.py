import math
OP = input('''Choose the operation that you need: \n+ for addition\n- for subtraction
* for multiplication\n/ for division\n** for exponentiation
log for math.log(x,(Base))\nceil for math.ceil\nfloor for math.floor\nR for round\n''')
number_a = float(input('Number "a" is: '))
number_b = float(input('Number "b" is: '))
n = int(input('Number "n" is: '))
if OP == '+':
    print(number_a+number_b)
elif OP == '-':
    print(number_a-number_b)
elif OP == '*':
    print(number_a * number_b)
elif OP == '/':
    if number_b == 0:
        print('Esche_ne_proshly ')
    else:
        print(number_a / number_b)
elif OP == '**':
    print(number_a ** number_b)
elif OP == 'log':
    print(math.log(number_a, number_b))
elif OP == 'ceil':
    print(math.ceil(number_a))
elif OP == 'floor':
    print(math.floor(number_a))
elif OP == 'R':
    print(round(number_a, n))
else:
    print('Error')

