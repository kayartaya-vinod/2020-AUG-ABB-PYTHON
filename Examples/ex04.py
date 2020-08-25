"""
Accept a number and print the factorial of the same.
"""

user_input = num = int(input('Enter a number: '))

fact = 1
while num >= 1:
    fact *= num  # fact = fact * num
    num -= 1  # num = num - 1

print('factorial of', user_input, 'is', fact)

# 5! + 4! + 3! + 2! =?
