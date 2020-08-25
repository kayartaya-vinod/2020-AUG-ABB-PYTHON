# Accept a number and print if it is even or odd

num = input('Enter a number: ')

# convert num into int
num = int(num)

if num % 2 == 0:
    print(num, 'is an even number!')
else:
    print(num, 'is an odd number')
