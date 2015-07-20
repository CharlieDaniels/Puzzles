#Given an integer, write a function to determine if it is a power of two

def power(x):
  #base case
  if x == 1:
  	return 1

  m = 1
  while m < x:
  	m = m * 2
  	if m == x:
  	  return 1
  return 0