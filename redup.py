'''Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.'''

def redup(array):
	i = 0
	while i < len(array)-1:
		if array[i] == array[i+1]:
			array.pop(i)
		else:
			i=i+1
	return array
