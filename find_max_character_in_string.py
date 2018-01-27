
"""
Return maximum occurring character in an input string

Write an efficient C function to return maximum occurring character in the input string e.g., if input string is “test” then function should return ‘t’
"""


def findmax(str1):
  d1 = {x : str1.count(x) for x in str1}
  sd1 = sorted(d1.items(), key = lambda x: x[1], reverse = True)
  print (sd1[0][0])
  
str1 = 'zzzaaaayfghvvtfa'
findmax(str1)
