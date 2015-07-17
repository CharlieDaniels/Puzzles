#find the longest palindrome word in a string
#example: 'hello anna how are you', Answer = anna

def findP(s):
  #split on spaces: make an array of strings
  s_arr = s.split(' ')
  #initialize hash table
  pal = {}
  #loop over each entry in array
  for word in s_arr:
    #define indices
    beg = 0
    end = len(word) - 1
    #determine if palindrome
    #import pdb;pdb.set_trace()
    #assume its a palindrome
    is_pal = 1
    while beg < end:
      if word[beg] != word[end]:
        is_pal = 0   
      beg += 1
      end -= 1
    #if it's a palindrome: store string as key, length as value
    if is_pal:      
        pal[word] = len(word)
  #return the key with the largest value
  return max(pal)

findP('hello anna how are you')