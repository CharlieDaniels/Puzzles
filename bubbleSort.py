#bubble sort
def bubblesort(A):
  #define terminating index
  term = len(A)
  #enter loop over shorter sections of array
  while term > 2:
  	#define comparative indices
    f = 0
    s = 1
  #enter comparitive loop
    while s < term:
  #if f>n swap and f & n and increase both indices
      if A[f] > A[s]:
      	A[f],A[s] = A[s],A[f]
      f = f+1
      s = s+1
    
    term = term - 1

  return A

B = [54, 26, 93, 17, 77]
bubblesort(B)