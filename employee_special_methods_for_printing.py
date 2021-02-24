#  OOP python wit manually set variables


class Employee:
    # class variables should be the same for all
    raise_amount = 1.04
    num_of_emps = 0

    #  this is like the constructor
    def __init__(self, first, last, pay):
        #  convention to call the instance as the first class self, then specify other args - instance variables unique for each instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        #  using self.raise_amount allows us to change the raise_amount for a single instance
        #  using self allows a sub class to override this variable
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    # dunder add special method
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


# print(Employee.num_of_emps)

#  creating instances of the employee class
#  self passed in automatically
emp_1 = Employee("Corey", "Schafer", 75000)
emp_2 = Employee("test", "user", 85000)

print(len(emp_1))

# print(repr(emp_1))
# print(str(emp_1))

# print(len('test'))
# print('test'.__len__())    #  dunder method __len__

#  dunder = double underscores
#  dunder init =  __init__

#  dunder add __add__()

# print(1 + 2)

# print(int.__add__(1, 3))  #  adds 2 values
# print(str.__add__("a", "b"))  #  concatenates 2 strings

# #  calculate total salaries by adding employees together
# print(emp_1 + emp_2)

