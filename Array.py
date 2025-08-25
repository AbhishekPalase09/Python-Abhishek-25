import array
arr = array.array('i', [1, 20, 30, 40,50,40])
print(arr)

#array functions

arr.append(6)
arr.insert(2,4)
arr.remove(4)
print(arr.pop(2))

print(arr.index(20))
arr.reverse()
print(arr)
print(arr.count(40))
print(arr.buffer_info())
print(arr.tolist())