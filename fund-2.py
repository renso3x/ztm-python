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
