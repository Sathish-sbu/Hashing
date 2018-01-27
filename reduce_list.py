"""
Converting array to reduced form

Input:  arr[] = {10, 40, 20}
Output: arr[] = {0, 2, 1}

Input:  arr[] = {5, 10, 40, 30, 20}
Output: arr[] = {0, 1, 4, 3, 2}

"""

def reduce(l1):
  temp = sorted(l1)
  tempcnt = [x for x in range(0, len(temp))]
  d1 = { x : y for x, y in zip(temp, tempcnt)}
  f = lambda x : d1[x]
  ret = [f(x) for x in l1]
  return ret
  
l1 = [10, 40, 20]
print (reduce(l1))
