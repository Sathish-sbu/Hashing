"""
Find Itinerary from a given list of tickets

Given a list of tickets, find itinerary in order using the given list.

Example:

Input:
"Cincinatti" -> "Boston"
"Philadelphia" -> "NYC"
"Hawai"    -> "Cincinatti"
"NYC"  -> "Hawai"

Output: 
Philadelphia->NYC, NYC->Hawai, Hawai->Cincinatti, Cincinatti->Boston

"""

def finditinerary(l1):
  s = dict(l1)
  l2 = [(x[1],x[0]) for x in l1]
  d =  dict(l2)
  src = [each for each in s if each not in d][0]
  res = []
  while len (res) != len (l1):
    res.append([src, s[src]])
    src = s[src]
  
  print (res)
  
  
  
l1 = [('Cincinatti', 'Boston'), ('Philadelphia', 'NYC'), ('Hawai', 'Cincinatti'), ('NYC', 'Hawai')]
finditinerary(l1)
