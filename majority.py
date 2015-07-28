#given an array of size n, find the majority element. The majority element is the element that
#appears more than n/2 times.

def majority(n):
	#create a hash table of the counts (value) of a number (key) in array n.
  h = {}
  for i in n:
    if i in h:
      h[i] = h.get(i) + 1
    else:
    	h[i] = 1
  if max(h.values())>len(n)/2:
  	return max(h.values())
  else:
  	return 0
