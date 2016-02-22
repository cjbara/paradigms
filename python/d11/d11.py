#! /usr/bin/python

# Name:  Cory Jbara
import csv
from employee import *

def giveEveryoneARaise(l):
	"""Gives everyone in l a raise of percentage"""
	for employee in l:
		employee.giveRaise()

def giveDeptARaise(l, dept):
	"""Gives everyone in dept a raise of percentage"""
	for employee in l:
		if employee.getDept() == dept:
			employee.giveRaise()

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
	onepercent = []
	top = []
	for e in l:
		top.append(e.getSalary())
	top.sort()
	total = int(.01 * len(l))
	threshold = top[-total]
	for e in l:
		if e.getSalary() >= threshold:
			onepercent.append(e)

	return onepercent

def reportMedAndAvg(l):
	"""Prints out the median and average salaries for the city"""
	median = getMedianSalary(l)
	avg = getAverageSalary(l)
	print "Median Salary:  $%.2f" % (median)
	print "Average Salary: $%.2f" % (avg)

def percentToEachClass(l):
	"""Prints out the percentage of the city's salary being paid to each of the employee classes"""
	asalary = 0
	absalary = 0
	csalary = 0
	totalsalary = 0
	for e in l:
		totalsalary += e.getSalary()
		if type(e) is EmployeeA:
			asalary += e.getSalary()
		elif type(e) is EmployeeAB:
			absalary += e.getSalary()
		elif type(e) is EmployeeC:
			csalary += e.getSalary()
	
	#compute each distribution and make sure they add to 100
	asalary = asalary / totalsalary * 100
	absalary = absalary / totalsalary * 100
	csalary = csalary / totalsalary * 100
	print "Percent salary for class A employees: %.2f%%" % (asalary)
	print "Percent salary for class C employees: %.2f%%" % (csalary)
	print "Percent salary for class AB employees: %.2f%%" % (absalary)
			

if __name__=="__main__":
	#read from roleclass.csv to determine the employee classes
	classes = {}
	f = open('roleclass.csv','r')
	for line in f:
		line = line.strip().split(',')
		classes[line[0]] = line[1]

	#read all employees into the array
	employees = []
	with open('chisalaries.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for person in reader:
			if not person['Name'] == '':
				salary = float(person['Employee Annual Salary'].strip('$'))
				eclass = classes[person['Position Title']]
				if eclass == 'A':
					employees.append(EmployeeA(person['Name'], person['Position Title'], person['Department'], salary))
				elif eclass == 'AB':
					employees.append(EmployeeAB(person['Name'], person['Position Title'], person['Department'], salary))
				elif eclass == 'C':
					employees.append(EmployeeC(person['Name'], person['Position Title'], person['Department'], salary))
	
	print "Initial salaries"
	percentToEachClass(employees)
	
	print "\nAfter Everyone's 5 raises"
	for _ in range(5):
		giveEveryoneARaise(employees)
	percentToEachClass(employees)
	print ""
	reportMedAndAvg(employees)
	
