#build pascals triangle up to row n

def pascal(n):
  #base cases
  if n == 1:
    pa = [1]
    return pa
  elif n == 2:
    pa = [[1],[1,1]]
    return pa

  #build initial triangle structure
  pa = [[]] * n
  pa[0] = [1]
  pa[1] = [1,1]  

  for g in range(2,len(pa)):
    pa[g] = [pa[g-1][0]]
    for h in range(len(pa[g-1])-1):
			pa[g].append(pa[g-1][h]+pa[g-1][h+1])
    pa[g].append(pa[g-1][-1])
  return pa
