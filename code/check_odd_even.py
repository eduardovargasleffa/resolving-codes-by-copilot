#  As input, receive an integer and check if it is odd or even. A tip is: use conditionals to perform the verification and, if possible, use Github Copilot (or another IA) to optimize the code structure. 

data = int(input('Enter an integer: '))

if data % 2 == 0:
    print(f'The number {data} is even.')
else:
    print(f'The number {data} is odd.')

# The code above checks if a number is odd or even. It takes an integer input from the user and uses the modulo operator to determine if the number is divisible by 2. If it is, the number is even; otherwise, it is odd. The result is printed to the console.

