'''
Find the largest prime factor of the number 600851475143
'''

#generate prime numbers < 600851475143
bigVal=21
#call prime function
import prime
primes=prime.prime(bigVal)
print('prime length=',len(primes))
x=len(primes)-2

for x in range(len(primes)-2,0):
  if bigVal%primes[x]==0:
    print(x)
    break
  else:
    x=x-1
print('x=',x)  
print('largest prime factor=',primes[x])
print(21%17)

