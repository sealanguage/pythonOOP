# /usr/bin/python3
#  OOP python with manually set variables


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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    #  new class method as an alternative constructor to parse the string
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)


#  new class, inherits variables/methods from Employee class
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super(Employee, self).__init__(self, first, last, pay, prog_lang)
        self.prog_lang = prog_lang


dev_1 = Developer("Corey", "Schafer", 75000, "Python")
dev_2 = Developer("test", "user", 85000, "Java")

#  customizing the sub class
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.email)
print(dev_1.prog_lang)

# print(
#     help(Developer)
# )  # resolution order walks up the chain of inheritance. the help will show all the inhertied properties/methods of Employee

