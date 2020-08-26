"""
Script to accept two numbers and print prime numbers between the same
"""


def is_prime(num):
    for n in range(2, num // 2 + 1):
        if num % n == 0:
            return False

    return True


def print_primes(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=', ')

    print()  # just a blank line


def main():
    n1 = int(input('Enter value for start: '))
    n2 = int(input('Enter value for end: '))

    print_primes(n1, n2)


if __name__ == '__main__':
    main()
