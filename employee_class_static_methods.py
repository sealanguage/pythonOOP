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


print(Employee.num_of_emps)

#  creating instances of the employee class
#  self passed in automatically
emp_1 = Employee("Corey", "Schafer", 75000)
emp_2 = Employee("test", "user", 85000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

