"""
Check if an array can be divided into pairs whose sum is divisible by k
Given an array of integers and a number k, write a function that returns true if given array can be divided into pairs such that sum of every pair is divisible by k.

Input: arr[] = {9, 7, 5, 3}, 
           k = 6
Output: True
We can divide array into (9, 3) and
(7, 5). Sum of both of these pairs 
is a multiple of 6.

Input: arr[] = {92, 75, 65, 48, 45, 35}, 
           k = 10
Output: True
We can divide array into (92, 48), (75, 65) 
and (45, 35). Sum of all these pairs is a
multiple of 10.

Input: arr[] = {91, 74, 66, 48}, k = 10
Output: False

"""

def checksumpairs(l, sum):
  d = {}
  for x in l:
    if x%sum not in d:
      d[x%sum] = 1
    else:
      d[x%sum] += 1
  
  for each in d:
    if sum - each not in d:
      return False
  
  return True

l = [92, 75, 65, 48, 45, 35]
print (checksumpairs(l, 10))
