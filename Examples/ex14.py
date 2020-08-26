class Product:

    def __init__(self, **kwargs):
        # print('type of kwargs is', type(kwargs))
        # print('kwargs contain', kwargs)
        self.id = kwargs.get('id', 0)  # invokes the setter for id
        self.name = kwargs.get('name', '')
        self.price = kwargs.get('price', 0.0)  # internally, __price is save as _Product__price

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if type(value) != int:
            raise TypeError('id must be a integer')
        if value < 0:
            raise ValueError('id must be >= 0')
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise TypeError('name must be a str')
        value = value.strip()  # remove leading/trailing white spaces
        ln = len(value)
        if ln > 50:
            raise ValueError('length of name must less than 50 letters')
        self.__name = value

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
        print('Price    : ₹', self.__price)  # self.__price --> self._Product__price
        print()

    # p1 += value
    def __iadd__(self, value):
        if type(value) in (int, float):
            self.price += value
        elif type(value) == str:
            self.name += value
        else:
            raise TypeError('Invalid type for += operation; expecting int, float or str, got {}'.format(type(value)))

        return self  # required for __iXXX__ operators (iXXX -> iadd, isub, imul, idiv, imod)

    def __gt__(self, value):
        if type(value) in (int, float):
            return self.price > value
        elif type(value) == Product:
            return self.price > value.price
        else:
            raise TypeError('Operator > cannot be used with Product and {}'.format(type(value)))

    def __str__(self):
        """
        Textually represents 'self'. Equivalent to toString() in Java/C#/JavaScript
        :return: textual representation of the current object (self)
        """
        return 'Product(id: {}, name: {}, price: {})'.format(self.__id, self.__name, self.__price)


def main():
    p1 = Product()
    p2 = Product(id=1, name='Cabbage', price=15.5)
    p3 = Product(name='Potato Organically Grown', price=52.5)
    p4 = Product(id=5, price=12.3)

    p1.display()
    p2.display()
    p3.display()
    p4.display()

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

    p3.display()


if __name__ == '__main__':
    main()
