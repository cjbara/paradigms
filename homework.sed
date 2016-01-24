# Name: Cory Jbara
# Date: January 20, 2016

# Programming Paradigms
# Regular Expression Primer

# Put each of your regular expressions under the headings below.  The file
# input.txt will be used for grading.  Your script should produce the same
# output as you see in output.txt.  You may test your script using sed:
# $ sed -n -E -f homework.sed input.txt
# Note that question 1 is already answered for you as an example.

# question 1
/do+g/p

# question 2
/(cat){5,7}([^c]|$)/p

# question 3
/^cat/p

# question 4
/^[^[:alnum:]]+mouse[^[:alnum:]]+$/p

# question 5
s/coward/hero/gp

# question 6
/[A-Za-z] ([0-9]{3}( |-)|\([0-9]{3}\)( |-)?)[0-9]{3}( |-)[0-9]{4}([^0-9]|$)/p
