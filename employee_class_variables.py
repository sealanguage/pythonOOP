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
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


#  creating instances of the employee class
#  self passed in automatically
emp_1 = Employee("Corey", "Schafer", 75000)
emp_2 = Employee("test", "user", 85000)


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# print(emp_1)
# print(emp_2)


# # print("{} {}".format(emp_1.first, emp_1.last))  //  changed to put in method above and still works in print statement below
# print(emp_1.fullname())
# #  this also works to print the employee name
# print(Employee.fullname(emp_1))
