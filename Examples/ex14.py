class Product:

    def __init__(self, **kwargs):
        # print('type of kwargs is', type(kwargs))
        # print('kwargs contain', kwargs)
        self.__id = kwargs.get('id')
        self.__name = kwargs.get('name')
        self.__price = kwargs.get('price', 0.0)  # internally, __price is save as _Product__price

    # getter property ( readonly variable)
    @property
    def price(self):
        return self.__price

    # setter property (writable variable)
    @price.setter
    def price(self, value):
        if type(value) not in (int, float):
            raise TypeError('price must be a number')
        if value < 0.0:
            raise ValueError('price must be >= 0.0')

        self.__price = value

    def display(self):
        # self is same as the invoking object (i.e, p1 or p2 from main)
        print('ID       :', self.__id)
        print('Name     :', self.__name)
        print('Price    : ₹', self.__price)   # self.__price --> self._Product__price
        print()

    def __str__(self):
        """
        Textually represents 'self'. Equivalent to toString() in Java/C#/JavaScript
        :return: textual representation of the current object (self)
        """
        return 'Product(id: {}, name: {}, price: {})'.format(self.__id, self.__name, self.__price)


def main():
    p1 = Product()
    p2 = Product(id=1, name='Cabbage', price=15.5)
    p3 = Product(name='Potato Organically Grown')
    p4 = Product(id=5, price=12.3)

    # p1.display()
    # p2.display()
    # p3.display()
    # p4.display()

    print(p1)  # --> print(p1.__str__())
    print(p2)
    print(p3)
    print(p4)

    print('attributes in p2 are:', dir(p2))

    p2.display()
    # p2.price = 'twenty'  # does not affect the self.__price
    # p2.__price = 'asdf'  # does not affect the self.__price
    # p2.display()

    # how do I change the value of p2.price???
    # p2.setPrice(45.6)  # typically, this is what you do in C++ or Java
    p2.price = 22.3  # --> invoke a setter property (which is nothing but a function)
    p2.display()


if __name__ == '__main__':
    main()