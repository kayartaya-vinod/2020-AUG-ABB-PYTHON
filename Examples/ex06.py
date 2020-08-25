"""
Example of 'for' loop print multiplication table for a value entered by the user
"""


def print_table(num, limit):
    for i in range(1, limit + 1):
        print("%d X %d = %d" % (num, i, num * i))


def main():
    n1 = int(input('Enter a value for num: '))
    l1 = int(input('Enter a value for limit: '))

    print_table(n1, l1)


# print('value of __name__ is', __name__)
# this must be conditionally called, so that if this module is
# imported in another module, which when run should not call this main()
if __name__ == '__main__':  # this is True only if you run this file (and not import)
    main()
