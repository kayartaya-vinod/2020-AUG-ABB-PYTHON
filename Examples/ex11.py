"""
Demonstration of creating classes and objects
"""


# Every class inherits many dunder attributes from a built-in class called object
class Product:

    def display(self):
        # self (or any other variable name), which is the first parameter of any member
        # function of any class, represents the invoking object
        print('Product details:')
        print('id of self is', id(self))


def main():
    # create an object of Product
    p1 = Product()
    print('id of p1 is', id(p1))
    print('attributes of p1 are: ', dir(p1))
    p1.display()  # p1 is a reference to an object product;
    # when p1.display() is called, p1 itself is passed as first argument to display() function
    # So, p1.display() --> Product.display(p1)
    Product.display(p1)


if __name__ == '__main__':
    main()
