""" 
Fibonacci Sequence - Recursion algorithm
Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
created by : khan safiq
"""


def fibonacci(number):
    # avoid unintentional case
    # assert number >= 0 and int(number) == number, 'Fibonacci sequence must be positive or not be decimal number'
  
    if number < 0:
        print('Fibonacci sequence must be positive or not be decimal number')
        number = int(input('Enter a number and have the program generate the Fibonacci sequence to that number: '))
        fibonacci(number)
    else:
        # base case -  avoid infinite recursion
        if number in [0,1]:
            return number
        else:
            # fibonacci flow case
            return fibonacci(number-1) + fibonacci(number-2)


process = True
number = input('Enter a number and have the program generate the Fibonacci sequence to that number: ')
while process:
    try:
        number = int(number)
        result = fibonacci(number)
        print('result:', result)
        break
    except ValueError:
        print('Fibonacci sequence must be positive or not be decimal number')
        number = input('Enter a number and have the program generate the Fibonacci sequence to that number: ')
        process = True