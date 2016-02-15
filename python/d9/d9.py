#! /usr/bin/python

# Name:  Cory Jbara
import csv

people = []
with open('chisalaries.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for person in reader:
		if not person['Name'] == '':
			people.append(person)

for index, person in enumerate(people):
	people[index]['Employee Annual Salary'] = float(person['Employee Annual Salary'].strip('$'))

total_payroll = 0
total_employees = 0
departments = []
for person in people:
	total_employees += 1
	total_payroll += person['Employee Annual Salary']
	departments.append(person['Department'])

average_yearly_pay = total_payroll/total_employees
departments = set(departments)

print 'Total payroll:{:>8}{:.2f}'.format('$',total_payroll)
print 'Number of employees:{:>15}'.format(total_employees)
print 'Average yearly pay:{:>8}{:.2f}'.format('$',average_yearly_pay)
print '\nNumber of city departments: {}'.format(len(departments))
print 'Names of city departments: {}'.format(" ".join(['"'+x+'"' for x in departments]))
