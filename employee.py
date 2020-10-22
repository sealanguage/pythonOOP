#  OOP python wit manually set variables


class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()

# print(emp_1)
# print(emp_2)

emp_1.first = "Corey"
emp_1.last = "Schafer"
emp_1.email = "corey.schafer@company.com"
emp_1.pay = 75000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "test.user@company.com"
emp_2.pay = 85000

print(emp_1.email)
print(emp_2.email)
