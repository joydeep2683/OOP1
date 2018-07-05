

# class Employee:


# 	num_of_emps = 0
# 	raise_amount = 1.04
# 	def __init__(self, first, last, pay):
# 		self.first = first
# 		self.last = last
# 		self.pay = pay
# 		self.email = first + "." + last + "@company.com"

# 		Employee.num_of_emps += 1

# 	"""For printing full name of employee"""
# 	def fullname(self):
# 		return f'{self.first} {self.last}'

# 	def apply_raise(self):
# 		self.pay = int(self.pay * self.raise_amount)

# print(Employee.num_of_emps)

# emp_1 = Employee('Joy', 'Deep', 50000)
# emp_2 = Employee('Jony', 'Deap', 60000)

# print(Employee.num_of_emps)

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

# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())
# print(emp_2.fullname())

# how a method inside a class works
# emp_1.fullname()
# print(Employee.fullname(emp_1))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print("raise_amount variable created")

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print("Increasing raise amount")

# Employee.raise_amount = 1.05

# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)



#-------------------------------------------------------------------------------



# class Employee:


# 	num_of_emps = 0
# 	raise_amount = 1.04
# 	def __init__(self, first, last, pay):
# 		self.first = first
# 		self.last = last
# 		self.pay = pay
# 		self.email = first + "." + last + "@company.com"

# 		Employee.num_of_emps += 1

# 	"""For printing full name of employee"""
# 	def fullname(self):
# 		return f'{self.first} {self.last}'

# 	def apply_raise(self):
# 		self.pay = int(self.pay * self.raise_amount)

# 	@classmethod
# 	def set_raise_amt(cls, amount):
# 		cls.raise_amount = amount

# 	@classmethod
# 	def from_string(cls, emp_str):
# 		first, last, pay = emp_str.split('-')
# 		return cls(first, last, pay)

# 	@staticmethod
# 	def is_workday(day):
# 		if day.weekday() == 5 or day.weekday() == 6:
# 			return False
# 		return True

# print(Employee.num_of_emps)

# emp_1 = Employee('Joy', 'Deep', 50000)
# emp_2 = Employee('Jony', 'Deap', 60000)

# print(Employee.num_of_emps)

# emp_str_1 = 'John-Doe-70000'

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# import datetime
# my_date = datetime.date(2018, 7, 22)
# print(Employee.is_workday(my_date))


#-------------------------------------------------------------------------------




class Employee:

	num_of_emps = 0
	raise_amount = 1.04
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@company.com"

		Employee.num_of_emps += 1

	"""For printing full name of employee"""
	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
	raise_amount = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang




dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Test', 60000, 'Java')

# print(help(Developer))

print(dev_1.prog_lang)
print(dev_2.prog_lang)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

















