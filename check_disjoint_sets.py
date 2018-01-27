"""
Find if two sets are disjoint 

Input: set1[] = {12, 34, 11, 9, 3}
       set2[] = {2, 1, 3, 5}
Output: Not Disjoint
3 is common in two sets.

Input: set1[] = {12, 34, 11, 9, 3}
       set2[] = {7, 2, 1, 5}
Output: Yes, Disjoint
There is no common element in two sets.

"""

def checkdisjointusinghashing(l1, l2):
  d1 = {x : 1 for x in l1}
  for each in l2:
    if each in d1:
      return False
  return True
  
def checkdisjoint(l1, l2):
  l1.sort()
  l2.sort()
  print (l1)
  print (l2)
  i = 0
  j = 0
  while (i < len(l1)) and (j  < len(l2)):
      print (l1[i] , l2[j])
      if l1[i] > l2[j]:
        j += 1
      elif l1[i] < l2[j]:
        i += 1
      else:
        return False
  
  return True
  

l1 = [12, 34, 11, 9, 3]
l2 = [2, 1, 34, 5, 2, 35]
print (l1)
print (l2)
#print (checkdisjoint(l1, l2))
print (checkdisjointusinghashing (l1,l2))
