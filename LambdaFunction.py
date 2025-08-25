square= lambda x: x*x

print(square(5))

#methods of Lambda
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, nums))
print(squares) 

nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)