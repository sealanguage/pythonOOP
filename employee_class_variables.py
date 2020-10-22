#  OOP python wit manually set variables


class Employee:
    #  this is like the constructor
    def __init__(self, first, last, pay):
        #  convention to call the instance as the first class self, then specify other args
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)


#  creating instances of the employee class
#  self passed in automatically
emp_1 = Employee("Corey", "Schafer", 75000)
emp_2 = Employee("test", "user", 85000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

# print("{} {}".format(emp_1.first, emp_1.last))  //  changed to put in method above
print(emp_1.fullname())
