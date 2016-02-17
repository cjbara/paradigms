# Name: Cory Jbara

class Employee(object):
	"""Base class for all employees, gets a default raise of 4%"""
	next_employee_number = 0
	
	def __init__(self, name, title, dept, salary):
		self.default_salary_inflator = 1.04
		self.name = name
		self.title = title
		self.dept = dept
		self.salary = salary
		self.employee_number = Employee.next_employee_number
		Employee.next_employee_number += 1
	
	def getName(self):
		return self.name

	def getTitle(self):
		return self.title

	def getDept(self):
		return self.dept
	
	def getSalary(self):
		return self.salary

	def getEmployeeNumber(self):
		return self.employee_number

	def setName(self, name):
		self.name = name

	def setTitle(self, title):
		self.title = title

	def setDept(self, dept):
		self.dept = dept

	def setSalary(self, salary):
		self.salary = salary

	def giveRaise(self):
		self.salary = self.salary * self.default_salary_inflator

	def __str__(self):
		return "[Employee name: %s, %s, %s, $%.2f]" % (self.name, self.title, self.dept, self.salary)

class EmployeeA(Employee):
	"""Class A employee, inherits from Employee, gets another raise of 2%"""
	def __init__(self, name, title, dept, salary):
		self.inflator_A = 1.02
		super(EmployeeA, self).__init__(name, title, dept, salary)

	def giveRaise(self):
		self.salary = self.salary * self.inflator_A * self.default_salary_inflator

	def __str__(self):
		return "[EmployeeA name: %s, %s, %s, $%.2f]" % (self.name, self.title, self.dept, self.salary)

class EmployeeC(Employee):
	"""Class C employee, inherits from Employee, gets another raise of 1%"""
	def __init__(self, name, title, dept, salary):
		self.inflator_C = 1.01
		super(EmployeeC, self).__init__(name, title, dept, salary)

	def giveRaise(self):
		self.salary = self.salary * self.inflator_C * self.default_salary_inflator

	def __str__(self):
		return "[EmployeeC name: %s, %s, %s, $%.2f]" % (self.name, self.title, self.dept, self.salary)

class EmployeeAB(EmployeeA):
	"""Class A employee, inherits from Employee, gets another raise of 2%"""
	def __init__(self, name, title, dept, salary):
		self.inflator_B = 1.08
		super(EmployeeAB, self).__init__(name, title, dept, salary)

	def giveRaise(self):
		self.salary = self.salary * self.inflator_B * self.inflator_A * self.default_salary_inflator

	def __str__(self):
		return "[EmployeeAB name: %s, %s, %s, $%.2f]" % (self.name, self.title, self.dept, self.salary)


