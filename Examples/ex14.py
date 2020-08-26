class Product:

    def __init__(self, **kwargs):
        # print('type of kwargs is', type(kwargs))
        # print('kwargs contain', kwargs)
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.price = kwargs.get('price', 0.0)

    def display(self):
        # self is same as the invoking object (i.e, p1 or p2 from main)
        print('ID       :', self.id)
        print('Name     :', self.name)
        print('Price    : ₹', self.price)
        print()

    def __str__(self):
        """
        Textually represents 'self'. Equivalent to toString() in Java/C#/JavaScript
        :return: textual representation of the current object (self)
        """
        return 'Product(id: {}, name: {}, price: {})'.format(self.id, self.name, self.price)


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


if __name__ == '__main__':
    main()
