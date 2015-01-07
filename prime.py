#This function takes n as an input and outputs all prime numbers between 2 and n.

def prime(n):
  primes = []
  fullrange = range(2,n+1)
  
  while fullrange:
    primes.append(fullrange.pop(0))
  
    i=0
    while (i<len(fullrange)):
      if fullrange[i]%primes[-1]==0:
        fullrange.pop(i)
        i=i-1 
      i=i+1
  
  print(primes)
  return

prime(200)