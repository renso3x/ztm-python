#Functional programming
from functools import reduce

#1. Map
my_list = [1,2,3]

def multiplyBy2(item):
  return item*2

print(list(map(multiplyBy2, my_list)))

#2. filter
def check_odd(item):
  return item % 2 == 0

print(list(filter(check_odd, my_list)))

#3. zip -> returns a tupple
you_list = [10,20,30]
another_list = [5, 13, 32]

print(list(zip(my_list, you_list, another_list)))

#4. reduce ->
def total_sum(acc, item):
  return acc + item

print(reduce(total_sum, my_list, 0))

#5. lambda expressions
#lambda param: action|perform operation
lambda_multiplier = lambda item: item*2
print(list(map(lambda_multiplier, my_list)))

#Excersice

# Square the list
my_list = [5,4,3]
print(list(map(lambda item: item*item, my_list)))
my_list.sort()
print(my_list)
# List Sorting
a = [(0, 2), (4, 3), (9,9), (10, -1)]
#option 1
print(sorted(a, key=lambda tup: tup[1]))
#option 2
a.sort(key=lambda x: x[1])
print(a)


# LIST COMPREHENSIONS

#param for param in iterable [if condition]
string = [x for x in 'hello']
print(string)
# add an expression square root
square_my_list = [num**2 for num in range(10)]
print(square_my_list)
# add an condition in your list
even_list = [num for num in range(10) if num % 2 == 0]
print(even_list)

# SET COMPREHENSIONS
# returns a distinct no duplicate
print({num for num in range(10) if num % 2 == 0})

# DICTIONARY COMPREHENSIONS
# key: value pairs .items()
# value .values()
# keys .keys()
simple_dict = {
  'a': 1,
  'b': 2
}
my_dict = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict)

my_dict = {num:num*2 for num in [1,2,3]}
print(my_dict)

# EXCERCISE return the list of duplicate
some_list = ['a','b','c','b','d','m','n','n']
duplicates = list(set(n for n in some_list if some_list.count(n) > 1))
print(duplicates)