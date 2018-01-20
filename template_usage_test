from string import Template

list1 = []
list1.append(dict(item = 'coke', price = 5, qty = 3))
list1.append(dict(item = 'rice', price = 25, qty = 1))
list1.append(dict(item = 'sweets', price = 3, qty = 10))
t = Template('$qty * $item = $price')
for data in list1:
  print (t.substitute(data))
