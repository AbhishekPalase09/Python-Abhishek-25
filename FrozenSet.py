s1 =  frozenset([1,2,3,4,2,1,5])    
s2 = frozenset(["apple","kiwi","melon",2,3])
s3 = frozenset([2,1])

#FrozenSet Functions

print(s1.union(s2))
print(s2.intersection(s1))
print(s1.difference(s2))
print(s1.issubset(s2))
print(s2.issubset(s1))
print(s1.issuperset(s2))
print(s1.issuperset(s3))
