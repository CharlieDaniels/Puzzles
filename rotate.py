#Given an array no, rotate it to the right by k steps. For example:
#array = [1,2,3,4,5,6,7] becomes new_array = [5,6,7,1,2,3,4]

def rotate(no,k):
	#take out the entries that will go up front
	array_slice = no[:-k]
	#reverse array
	array_slice = array_slice[::-1]
	#add the last entries onto the front
	for i in range(1,k+1):
	  array_slice.append(no[-i])

	return array_slice[::-1]