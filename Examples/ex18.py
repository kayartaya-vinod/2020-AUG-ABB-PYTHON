def factorial(num):
    # assert num > 0, 'num must be >0'
    # if not num > 0: raise AssertionError('num must be >0')

    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


def fibonacci(index):
    # f(0)=0, f(1)=1, f(n)=f(n-1)+f(n-2)
    assert index >= 0, 'Index must be >=0'
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)
