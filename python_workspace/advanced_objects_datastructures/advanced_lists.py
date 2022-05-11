l = [1, 2, 3]
l.append(4)
print(l)
# append adds the entire list to an element in itself i.e append just the entire iterable
x = [1, 2, 3]
y = [4, 5, 6]
x.append(y)
# [1, 2, 3, [4, 5, 6]]
print(x)
# extend will append each element in that iterable i.e. appends elements individually from that iterable
x = [1, 2, 3]
y = [4, 5, 6]
x.extend(y)
# [1, 2, 3, [4, 5, 6]]
print(x)
l = ['a', 'b', 'c', 'd', 'b']
# counts how many times an object occurs in the list
# 2
print(l.count('b'))
l = ['a', 'b', 'c', 'd']
# 2nd index postion
print(l.index('c'))
# ValueError: 'e' is not in list
# print(l.index('e'))
# ['a', 'b', 'INSERTED', 'c', 'd']
# insert takes in 2 arguments: insert(index,object) -> This method places the object at index supplied
l.insert(2, 'INSERTED')
print(l)
# pops off the last element off the list. the change is permanent
popped_elt = l.pop()
# d
print(popped_elt)
# ['a', 'b', 'INSERTED', 'c']
print(l)
# you can also pass an index into pop
popped_elt = l.pop(1)
# b
print(popped_elt)
# ['a', 'INSERTED', 'c']
print(l)
l = ['a', 'b', 'c', 'd', 'b']
# remove removes the first occurance of the value
l.remove('b')
# ['a', 'c', 'd', 'b']
print(l)
l = ['a', 'b', 'c', 'd']
# reverses the elements in place. affects your list permanently
l.reverse()
# ['d', 'c', 'b', 'a']
print(l)
l = ['d', 'b', 'a', 'c']
# sorts the elements in place. affects your list permanently
l.sort()
# ['a', 'b', 'c', 'd']
print(l)
