s = set()
s.add(1)
s.add(1)
s.add(2)
# {1, 2}
print(s)
# clear elements from set
s.clear()
# set()
print(s)
s.add(2)
s.add(3)
s.add(3)
# copy/clone a set
sc = s.copy()
s.add(4)
# {2, 3}
print(sc)
# difference between 2 sets
# {4}
print(s.difference(sc))
s1 = {'a', 'b', 'c', 'd', 'e'}
s2 = {'d', 'e'}
# returns the first set after removing all the elements found in the second one
s1.difference_update(s2)
# {'a', 'b', 'c'}
print(s1)
s = {1, 2, 3, 4}
# discards an element if it is a member of the set, otherwise does nothing
s.discard(3)
# {1, 2, 4}
print(s)
s1 = {'a', 'b', 'c', 'd', 'e'}
s2 = {'d', 'e'}
# returns the common elements between 2 sets
# {'e', 'd'}
print(s1.intersection(s2))
# updates the set with only the common elements, rest are discarded
s1.intersection_update(s2)
# {'e', 'd'}
print(s1)
# returns true if the elements between 2 sets have null intersection
s1 = {1, 2, 3}
s2 = {1, 2, 4}
s3 = {5, 6, 7}
# False
print(s1.isdisjoint(s2))
# True
print(s1.isdisjoint(s3))
s1 = {1, 2, 3}
s2 = {1, 2}
# True
print(s2.issubset(s1))
# True
print(s1.issuperset(s2))
# Returns the elements that is exactly in one of the sets
# {3}
print(s1.symmetric_difference(s2))
s1 = {1, 2, 3}
s2 = {1, 2, 4, 5}
# returns the union of 2 sets
# {1, 2, 3, 4, 5}
print(s1.union(s2))
# updates a set with a union of itself and others
s1 = {1, 2, 3}
s2 = {1, 2, 4, 5}
s1.update(s2)
# {1, 2, 3, 4, 5}
print(s1)
