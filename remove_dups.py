"""
Print all distinct elements of a list

Input: arr[] = {12, 10, 9, 45, 2, 10, 10, 45}
Output: 12, 10, 9, 45, 2

Input: arr[] = {1, 2, 3, 4, 5}
Output: 1, 2, 3, 4, 5

Input: arr[] = {1, 1, 1, 1, 1}
Output: 1

"""

def finddistincts(l1):
  d1 = {}
  f = lambda x : x not in d1
  d1 = {x : 1 for x in l1 if f(x)}
  f = lambda x : x[0]
  ret = [f(x) for x in d1.items()]
  print (ret)
  
l1 = [12, 10, 9, 45, 2, 10, 10, 45]
finddistincts(l1)
