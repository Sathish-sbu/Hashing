"""
Given an array of pairs, find all symmetric pairs in it
2.4
Two pairs (a, b) and (c, d) are said to be symmetric if c is equal to b and a is equal to d. For example (10, 20) and (20, 10) are symmetric. Given an array of pairs find all symmetric pairs in it.

It may be assumed that first elements of all pairs are distinct.

Example:

Input: arr[] = {{11, 20}, {30, 40}, {5, 10}, {40, 30}, {10, 5}}
Output: Following pairs have symmetric pairs
        (30, 40)
        (5, 10)  
        
"""


def findsymetricpairs(list1):
  d1 = {}
  result = list()
  for each in list1:
    temp = list()
    temp.append(each[1])
    temp.append(each[0])
    if str(temp) in d1.keys():
      result.append(each)
      result.append(temp)
    if str(each) not in d1.keys():
      d1[str(each)] = 1
      
  print (result)
    
  
list1 = [[11,20], [30,40], [5,10], [40,30], [10,5]]
findsymetricpairs(list1)
