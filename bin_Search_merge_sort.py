"""
Mergesort & Binsearch

"""

def merge(s1, s2):
  i = 0
  j = 0
  r = []
  while i < len(s1) and j < len(s2):
    if s1[i] < s2[j]:
      r.append(s1[i])
      i += 1
    elif s1[i] >= s2[j]:
      r.append(s2[j])
      j += 1
  
  if i < len(s1):
    r.extend(s1[i:])
  if j < len(s2):
    r.extend(s2[j:])
    
  return r
  
def mergesort(l1, start, end):
  print ('merge sorting ' + str(start) + ' and ' + str(end))
  if start == end:
    return [l1[start]]
  elif start  == end - 1:
    return [l1[start], l1[end]] if l1[start] <= l1[end] else [l1[end], l1[start]]
  else:
    mid = int((start + end)/2)
    s1 = mergesort(l1,start,mid)
    s2 = mergesort(l1,mid+1,end)  
    return merge(s1,s2)
  
