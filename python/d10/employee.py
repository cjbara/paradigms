# Name: Cory Jbara

class Employee:
	
	next_employee_number = 0
	
	def __init__(self, name, title, dept, salary):
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

	def giveRaise(self, percentage):
		percentage = 1 + (.01 * percentage)
		self.salary = self.salary * percentage

	def __str__(self):
		return "[Employee name: {}, {}, {}, ${:.2f}]".format(self.name, self.title, self.dept, self.salary)
