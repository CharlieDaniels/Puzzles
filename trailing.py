#Given an integer n, return the number of trailing zeroes in n!

from math import factorial

def trailing(n):
	#find the factorial of n
	f = factorial(n)
	#cast it as a string
	f_string = str(f)
	#initialize counters
	num_zeroes = 0
	counter = -1
	#count the number of zeroes in n, starting from the end
	while f_string[counter] == '0':
		num_zeroes = num_zeroes + 1
		counter = counter -1

	return num_zeroes
