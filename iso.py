#Given two strings determine if they are isomorphic
#examples of isomorphs: 'egg', 'add'

def iso(s,t):
	#if they aren't the same length, they aren't isomorphs
	if len(s) != len(t):
		return 'nonisomorph'
	h={}
	for i in range(len(s)):
		#first check if c1 is already stored in hash table
		if s[i] in h:
			#if it's in the hash table, check that the value is c2
			if h[s[i]] != t[i]:
				return 'nonisomorph'
		h[s[i]]=t[i]
	return 'isomorph'