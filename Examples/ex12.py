class Product:

    def __init__(self):
        # this is a special function, that is called automatically when an object of this class is created
        # print('Inside Product.__init__(..) id of self is', id(self))
        self.id = 1
        self.name = 'Apple fuji'
        self.price = 210.0

    def display(self):
        # print('id of self in Product.display(..) is', id(self))
        print('ID       :', self.id)
        print('Name     :', self.name)
        print('Price    : ₹', self.price)
        print()


def main():
    p1 = Product()
    # 1. memory is allocated required for an object, with an id
    # 2. python will automatically invoke __init__ of Product class, by supplying the newly generated id
    # 3. returns the id of the newly created object, which then is assigned to p1 in line main()
    print('id of p1 is', id(p1))
    # print(dir(p1))
    p1.display()

    p2 = Product()
    p2.display()


if __name__ == '__main__':
    main()
