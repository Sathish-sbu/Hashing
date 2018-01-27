"""
count pairs with given sum 

Examples:
Input  :  arr[] = {1, 5, 7, -1}, 
          sum = 6
Output :  2
Pairs with sum 6 are (1, 5) and (7, -1)

Input  :  arr[] = {1, 5, 7, -1, 5}, 
          sum = 6
Output :  3
Pairs with sum 6 are (1, 5), (7, -1) &
                     (1, 5)         

Input  :  arr[] = {1, 1, 1, 1}, 
          sum = 2
Output :  6
There are 3! pairs with sum 2.

Input  :  arr[] = {10, 12, 10, 15, -1, 7, 6, 
                   5, 4, 2, 1, 1, 1}, 
          sum = 11
Output :  9

"""

def findsumpairs(l1, s):
  d1 = {}
  for each in l1:
    d1[each] = d1[each] + 1 if each in d1 else 1
  c =0
  for each in l1:
    if sum - each in d1 :
      c += d1[sum-each]
    if each == sum - each:
      c -= 1
    
  return int(c/2)
  

l1 = [1,1,1,1]
sum = 2

print (findsumpairs(l1,sum))
