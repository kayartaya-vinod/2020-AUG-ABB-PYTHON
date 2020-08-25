"""
Utility functions by Vinod <vinod@vinod.co>

Some example utility functions available for use:
1. factorial
"""

import json


def csv_2_json(filename):
    """
    Converts a CSV file into a JSON file with the same name

    :param filename: name with absolute or relative path of the file containing CSV data
    :return: None
    """

    data = []

    # f.close() is automatically called when the 'with' block exits
    with open(filename) as f:
        header = f.readline().strip().split(',')
        # TODO: convert the following for loop into a list comprehension
        for line in f:
            value = line.strip().split(',')
            data.append(dict(zip(header, value)))

        json_file = filename[:-3] + 'json'
        with open(json_file, 'w') as outfile:
            json.dump(data, outfile, indent=4)


def factorial(num):
    """
    Factorial of a given number.
    Factorial of a number is the product of all numbers between 1 and itself
    :param num: number for which you want factorial
    :return: factorial of the input number
    """

    fact = 1
    while num >= 1:
        fact *= num  # fact = fact * num
        num -= 1  # num = num - 1

    return fact


def dirr(obj):
    """
    Returns a list consisting of non-dunder attributes in obj
    :param obj: Object for which we want list of non-dunder attributes
    :return: list of non-dunder attributes in obj
    """
    attributes = dir(obj)
    ret_list = []
    for attr in attributes:
        if not attr.startswith('_'):
            ret_list.append(attr)

    return ret_list


if __name__ == '__main__':
    csv_2_json('customers.csv')

    # sum_of_fact_5_7 = factorial(5) + factorial(7)
    # print('5! + 7! is', sum_of_fact_5_7)
