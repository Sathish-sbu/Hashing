
"""
Longest consecutive subsequence

"""

def findconsecutivesubseq(l):
  l.sort()
  c = 1
  maxc = 0
  i = 0
  while (i < len(l) -1 ):
    if l[i+1] - l[i] == 1:
      i += 1
      c += 1
    else:
      c = 0
      i += 1
    maxc = c if c >= maxc else maxc
  
  return maxc
  
def findconsecutivesubseq_1(l):
  d1 = {x:1 for x in l}
  maxc = 0
  for d in d1:
    if (d-1 not in d1):
      c = 1
      while d+1 in d1:
        c += 1
        d += 1
        
    maxc = max(c,maxc)  
  return maxc
      

input = [12,4,42,32,542,13]
print (findconsecutivesubseq(input))
print (findconsecutivesubseq_1(input))
