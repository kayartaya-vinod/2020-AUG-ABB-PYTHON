from ex14 import Product


def main():
    p1 = Product(id=1, name='Beet root', price=29.0)
    p1.display()

    p1.price = 32.0
    p1.display()

    p1.price += 5  # p1.price = p1.price + 5
    p1.display()

    p1 += ', organically grown'  # expectation: name should be appended with ', organically grown'
    p1 += 5  # want p1.price to be incremented by ₹5
    p1.display()

    p2 = Product(id=2, name='Carrot', price = 49)
    if p1 > p2:
        print('{} is expensive than {}'.format(p1.name, p2.name))
    else:
        print('{} is not expensive than {}'.format(p1.name, p2.name))

    if p1 > 50:
        print('%s is costly' % p1.name)
    else:
        print('%s is cheap' % p1.name)

    # if p1 > 'one million':
    #     print('%s is costly' % p1.name)
    # else:
    #     print('%s is cheap' % p1.name)


if __name__ == '__main__':
    main()
