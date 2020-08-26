# according the book on OOP by Grady Booch, 4 major OOP elements, 3 minor elements
# 1. abstraction <-- hide implementation details
# 2. encapsulation <-- access restriction (java/c++/c# --> private/public/protected) (python _ protected, __ private)
# 3. hierarchy <-- arrangement of classes for code reuseability
#    (aggregation HAS-A, inheritance IS-A, association USES-A)
# 4. modularity <-- functions/classes

# 5. typing <-- provision to create data types
# 6. persistence <-- ability of a language to persist primary memory content into secondary memory
# 7. concurrency <-- ability of a language to do multiple things in a way of 'together'

# class Person inherits from class 'object'
class Person(object):

    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__gender = kwargs.get('gender', 'Male')

    def display(self):
        # title = self.__gender=='Male' ? 'Mr.': 'Ms.'
        title = 'Mr.' if self.__gender == 'Male' else 'Ms.'
        print('Name      : {}{}'.format(title, self.__name))


class Employee(Person):

    def __init__(self, **kwargs):
        # Person.__init__(self, **kwargs)
        super().__init__(**kwargs)
        self.__id = kwargs.get('id')
        self.__salary = kwargs.get('salary', 35000.0)

    def display(self):
        print('ID        : {}'.format(self.__id))
        # Person.display(self)
        super().display()
        print('Salary    : {}'.format(self.__salary))


class Manager(Employee):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__proj_lst = []

    # for setter property, a getter property must exist
    @property
    def projects(self):
        return self.__proj_lst

    @projects.setter
    def projects(self, proj_lst):
        if type(proj_lst) != list:
            raise TypeError('Projects must be of class list')
        self.__proj_lst = proj_lst

    def display(self):
        super().display()
        print('Current projects: {}'.format(self.projects))


def main():
    e1 = Employee(id=7788, name='Ramesh Iyer', salary=57900.0)
    e1.display()

    print('-=-'*20)
    e2 = Employee(id=6543, gender='Female', name='Asha', salary=65400.0)
    e2.display()

    print('-=-' * 20)
    m1 = Manager(id=6789, gender='Female', name='Nalini', salary=77800.0)
    m1.projects.append('XYZ')
    m1.projects.append('MIRA')
    m1.projects.append('LUNA')
    m1.display()


if __name__ == '__main__':
    main()
