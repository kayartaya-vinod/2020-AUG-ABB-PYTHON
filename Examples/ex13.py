class Product:

    def __init__(self, id=None, name=None, price=0.0):
        self.id = id  # a new attribute 'id' created in this object
        self.name = name  # a new attribute 'name' created in this object
        self.price = price  # a new attribute 'price' created in this object

    def display(self):
        # self is same as the invoking object (i.e, p1 or p2 from main)
        print('ID       :', self.id)
        print('Name     :', self.name)
        print('Price    : ₹', self.price)
        print()


def main():
    p1 = Product(1, 'Apple Fuji', 210.0)
    p2 = Product(5, 'Potato Organically grown', 52.0)
    p3 = Product()
    p4 = Product(12, 'Cabbage')

    p1.display()
    p2.display()
    p3.display()
    p4.display()


if __name__ == '__main__':
    main()
