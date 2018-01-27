"""
Given an unsorted array that may contain duplicates. Also given a number k which is smaller than size of array. 
Write a function that returns true if array contains duplicates within k distance.

Input: k = 3, arr[] = {1, 2, 3, 4, 1, 2, 3, 4}
Output: false
All duplicates are more than k distance away.

Input: k = 3, arr[] = {1, 2, 3, 1, 4, 5}
Output: true
1 is repeated at distance 3.

Input: k = 3, arr[] = {1, 2, 3, 4, 5}
Output: false

Input: k = 3, arr[] = {1, 2, 3, 4, 4}
Output: true
"""

def checkdups(list1, k):
  print ('checking dups in ' + str(list1))
  chk = list()
  for each in list1:
    if each in chk:
      return True
    else:
      chk.append(each)
    if len(chk) > k:
      del chk[0]
  
  return False
    
list1 = [1,2,3,4,1,2,3,4]
list2 = [1, 2, 3, 1, 4, 5]
list3 = [1, 2, 3, 4, 5]
list4 = [1, 2, 3, 4, 4]
print (checkdups(list1,3))
print (checkdups(list2,3))
print (checkdups(list3,3))
print (checkdups(list4,3))
