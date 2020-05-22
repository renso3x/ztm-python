#Fundamentals No.2
#Data Structure

# 1. Lists
li = [1,4,5,6,23]
print(li)
li2 = ['a', 'b','cd', 23]
print(li2)
#Find index of value
print(li2.index('cd'))
#Safe to return Boolean
print(1 in li2)
print(23 in li2)

# List slicing
amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
]
#copying the array which you are changing mutable
new_cart = amazon_cart
#copy the list immutable [:]
new_cart_copy = new_cart[:]
new_cart_copy[0] = 'test'
print(amazon_cart[0::2])
print(new_cart)
print(new_cart_copy)
#return no. of this values
# print(amazon_cart)
#modifies the list
# amazon_cart.sort()
# print(amazon_cart)
# sorted creates a new list
print(sorted(amazon_cart))
print(amazon_cart)
print(amazon_cart.count('noteboo'))

# Common List Patterns
# len(list)
# list[::-1] -> reverse
# list.revese()
# range(start, stop)
# list.join(['', '!']) -> creates new list

# List Unpacking
a,b,c, *rest = [1,2,3,4,5,6]
print(a)
print(b)
print(c)
print(rest)

#Dictionary
my_dict = {
  'name': 'Romeo',
  'age': 26,
  'address': 'Manila'
}
if (not 'address' in my_dict.keys()):
  print('Not found')
else:
  print(my_dict['address'])

#access value in dict
print(my_dict.get('age'))


#TUPLE
my_tuple = (1,2,3,4,5,1)
print(my_tuple[2])

x,y,z, *other = my_tuple
print(other)
print(my_tuple.count(1)) #count all the same value
print(my_tuple.index(2)) #find the first value
print(len(my_tuple))

#SET -> unique values
my_set = {1,2,3,4,5, 5}
my_set.add(100)
new_set = my_set.copy()
my_set.clear()
print(my_set)
print(new_set)


# for loops
for item in 'Zero to mastery': #strings
  print (item)

for i in [1,2,3,4]: #list
  print(i)

for i in (1,23,4): #sets
  print (i)

#iterate a dictionary
user = {
  "name": 'GOlem',
  "age": 32,
  "can_swim": False
}
#items() returns a tuple (key, value)
for k, v in user.items():
  print(k, v)

#Excercise
total = 0

for i in range(11):
  total += i

print('Total ', total)

#enumrate - can be a list, string, set
for i, c in enumerate("Hello"):
  print (i, c)

for i,c in enumerate(list(range(100))):
  if (c == 50):
    print(f'index of 50 is: {i}')

for i,c in enumerate((1,23,45,6)):
  print(f'{i} set {c}')

# while loops
i = 0
while i < 50:
  print (i)
  i += 1
else:
  print ('done printing the loop')

for i in range(10):
  print(i)
else:
  print('yesss----')


# functions
def print_my_number(*args):
  print(args)

print_my_number(2,3)

def print_my_key_args(**kwargs):
  #kwargs are dict to access it
  # Result: {'first_name': 'Romeo', 'last_name': 'Enso', 'age': 2}
  print(kwargs['first_name'])
  print(kwargs['last_name'])
  print(kwargs['age'])

print_my_key_args(first_name="Romeo", last_name="Enso", age=2)

#List Comprehension
#1.Compute a cube of a number
nums = [1,2,3,4,5]
cube_nums = []

for n in nums:
  cube_nums.append(n**3)

print(cube_nums)

#Alternative
cube_nums = [n**3 for n in nums]
print(f'Alternative to list comprehension {cube_nums}' )

#2.if it is greater than 3
new_list = []
for n in nums:
  if (n > 3):
    new_list.append(n**3)

print(f'If greater than 3 {new_list}' )

new_list = [n**3 for n in nums if n > 3]
print(f'Alternative If greater than 3 {new_list}' )


# 3. calling functions with list comprehensions
def cube(n):
  return n**3

new_list = [cube(n) for n in nums if n > 3]

print(f'Alternative using function If greater than 3 {new_list}' )


# LAMBDA
#lambda arguments : expression
cube = lambda n: n**3
print(cube(2))

#expononential
exponnential = lambda multiplier, number, exponent: multiplier * number ** exponent
print(exponnential(2,2,3))

#build in function
# list and map
num = [2,5,10]
print(list(map(lambda n: n**3, num)))

# list and filter
print(list(filter(lambda n: n > 5, num)))


# Modules

import math as m

print(m.e)

print (m.sqrt(9))

# Importing basic_operation module
import basic_operations

print(basic_operations.add(5, 5))
print(basic_operations.subtract(5, 3))
print(basic_operations.multiply(5, 3))
print(basic_operations.divide(5, 3))
