#  OOP python wit manually set variables


class Employee:
    # class variables should be the same for all
    raise_amount = 1.04

    #  this is like the constructor
    def __init__(self, first, last, pay):
        #  convention to call the instance as the first class self, then specify other args - instance variables unique for each instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        #  using self.raise_amount allows us to change the raise_amount for a single instance
        #  using self allows a sub class to override this variable
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


#  creating instances of the employee class
#  self passed in automatically
emp_1 = Employee("Corey", "Schafer", 75000)
emp_2 = Employee("test", "user", 85000)


print(Employee.raise_amount)

#  prints {'pay': 75000, 'last': 'Schafer', 'email': 'Corey.Schafer@company.com', 'first': 'Corey'}  no raise_amount in the dict
# print(emp_1.__dict__)

#  changes raise amount as class variable
Employee.raise_amount = 1.05

# changes raise_amount for just the instance
emp_1.raise_amount = 1.08


#  prints out  {'pay': 75000, 'last': 'Schafer', 'email': 'Corey.Schafer@company.com', 'first': 'Corey'}  {'__module__': '__main__', '__init__': <function __init__ at 0x10c5757d0>, 'raise_amount': 1.04, 'fullname': <function fullname at 0x10c575ed8>, '__doc__': None, 'apply_raise': <function apply_raise at 0x10c579d70>}  which has access to the class attribute raise_amount
# print(Employee.__dict__)

#  instance accesses the classes attribute
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# print(emp_1)
# print(emp_2)


# # print("{} {}".format(emp_1.first, emp_1.last))  //  changed to put in method above and still works in print statement below
# print(emp_1.fullname())
# #  this also works to print the employee name
# print(Employee.fullname(emp_1))
