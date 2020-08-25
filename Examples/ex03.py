"""
Print the number of days in the given month.

If the  input is not a valid month number then, print an error message
"""

month = int(input('Enter a number (1 - 12) representing a month: '))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("There are 31 days for the month", month)
elif month in [4, 6, 9, 11]:
    print("There are 30 days for the month", month)
elif month == 2:
    print("There are 28 or 29 days for the month", 2)
else:
    print("Invalid value for month. Must be between 1 to 12, got", month)

print("This is the end of the script")
