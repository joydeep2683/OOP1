



class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@company.com"

	"""For printing full name of employee"""
	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * 1.04)

emp_1 = Employee('Joy', 'Deep', 50000)
emp_2 = Employee('Jony', 'Deap', 60000)

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Joy'
# emp_1.last = 'Deep'
# emp_1.email = 'joy.deep@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Jony'
# emp_2.last = 'Deap'
# emp_2.email = 'jony.deap@company.com'
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())

# how a method inside a class works
emp_1.fullname()
print(Employee.fullname(emp_1))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)











