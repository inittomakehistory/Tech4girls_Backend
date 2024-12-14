# python basics 
# append()
example 
lists = [1, 2, 3, 4, 5]
lists.append("6")
print(lists)

# remove()
lists = [1, 2, 3, 4, 5]
lists.remove(4)
print(lists)

# pop()
lists = [1, 2, 3, 4, 5]
lists.pop(4)
print(lists)

# sort ()
lists = [1, 2, 3, 4, 5]
lists.sort()
print(lists)

# reverse ()
lists = [1, 2, 3, 4, 5]
lists.reverse()
print(lists)

# extend
lists = [1, 2, 3, 4, 5]
lists.extend([6,7])
print(lists)

# add()
lists = [1, 2, 3, 4, 5]
lists.insert(4,"four")
print(lists)

# remove()
lists = [1, 2, 3, 4, 5]
lists.remove(3)
print(lists)

# union()
setA = {1, 2, 3}
setB = {4, 5, 6}
union_set = setA | setB
print(union_set)

# intersection()
setA =  {1, 2, 3}
setB = {4, 5, 6}
intersection_ set = setA & setB 
print(intersection_set)

# difference()
setA =  {1, 2, 3}
setB = {4, 5, 6}  
difference_set =  setA - setB 
print(difference_set)

