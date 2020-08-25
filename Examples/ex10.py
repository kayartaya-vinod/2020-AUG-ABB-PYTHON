"""
Demonstration of handling exceptions (runtime errors)
"""

import sys


def main():
    # print('Command line arguments are', sys.argv)
    try:
        arg1, arg2 = sys.argv[1], sys.argv[2]
        num, den = int(arg1), int(arg2)
        quotient = num/den
        print('{} / {} = {}'.format(num, den, quotient))
    except IndexError:
        print('Two inputs expected')
        return
    except ValueError:
        print('Only int values expected')
    except ZeroDivisionError:
        print('Cannot divide a number by zero')
    except Exception:
        print('Something went wrong!')
    finally:
        # typically used for closing any open resources such as files, network sockets and db objects
        print('This is executed always')

    print('End of script')


if __name__ == "__main__":
    print('calling main...')
    main()
    print('finished calling main!')
