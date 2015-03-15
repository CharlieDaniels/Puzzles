'''
By considering the terms in the Fibonacci sequence 
whose values do not exceed four million, find the sum of 
the even-valued terms.
'''

#Generate the Fibonacci series
fib=[1,2]
#fib=fib.append(3) CANT DO THAT. Returns "none"
i=0
while fib[i]<4000000:
  fib.append(fib[i]+fib[i+1])
  i=i+1

evenfib=[]
j=0
for j in range(0,len(fib)):
  if fib[j]%2==0:
    evenfib.append(fib[j])
  j=j+1

evenfibsum=sum(evenfib)
print(evenfibsum)
