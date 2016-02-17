#! /usr/bin/python

# Name:  Cory Jbara
import csv
from employee import Employee

def giveEveryoneARaise(l, percentage):
	"""Gives everyone in l a raise of percentage"""
	for employee in l:
		employee.giveRaise(percentage)

def giveDeptARaise(l, dept, percentage):
	"""Gives everyone in dept a raise of percentage"""
	for employee in l:
		if employee.getDept() == dept:
			employee.giveRaise(percentage)

def getHighestSalary(l):
	"""Returns the employee in l with the highest salary"""
	highest = Employee("Test", "Test", "test", 0)
	for e in l:
		if e.getSalary() > highest.getSalary():
			highest = e
	return e

def getAverageSalary(l):
	"""Returns the average salary of all employees in l"""
	total = len(l)
	salary = 0
	for e in l:
		salary += e.getSalary()
	return salary/total

def getMedianSalary(l):
	"""Returns the median salary in l"""
	salary = []
	for e in l:
		salary.append(e.getSalary())
	salary.sort()
	if len(salary)%2 == 0:
		one = salary[len(salary)/2]
		two = salary[len(salary)/2 + 1]
		return (one + two)/2
	else:
		return salary[len(salary)/2]

def getOnePercent(l):
	"""Returns a list of all employees in the top one percent of income"""
	onepercent = sorted(l)
	total = int(.01 * len(l))
	onepercent = onepercent[-total:]

	return onepercent

def reportMedAndAvg(l):
	"""Prints out the median and average salaries for the city"""
	median = getMedianSalary(l)
	avg = getAverageSalary(l)
	print "Median Salary:  ${:.2f}".format(median)
	print "Average Salary: ${:.2f}".format(avg)

if __name__=="__main__":
	employees = []
	with open('chisalaries.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for person in reader:
			if not person['Name'] == '':
				salary = float(person['Employee Annual Salary'].strip('$'))
				employees.append(Employee(person['Name'], person['Position Title'], person['Department'], salary))
	
	print "Baseline"
	reportMedAndAvg(employees)
	giveEveryoneARaise(employees, 5)
	
	print "\nAfter Everyone's 5% raise"
	reportMedAndAvg(employees)
	
	print "\nAfter FIRE department's 6% raise"
	giveDeptARaise(employees, "FIRE", 6)
	reportMedAndAvg(employees)
	
	print "\nTop 1%'s median and average income"
	top = getOnePercent(employees)
	reportMedAndAvg(top)
