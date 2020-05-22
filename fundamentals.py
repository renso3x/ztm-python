#### Fundamental Data Types ####

print(type(6))

print(type(2-4))

print(type(2*4))

print(type(2/4))

print (2**2) #exponential 2 * 2 * 2

print (2 // 4) #round to an integer

#modulo - return the remainder of the division
print (5 % 4)

#Math functions

print(round(3.1))

print(round(3.9))

print(abs(-2123123.32))



#### OPERATOR PRECEDENCE ####

# ()
# **
# * /
# + -

# 3 * 4 gets evaluated
# 20 - 12 = 8
print(20 - 3 * 4)

#17 + 8 = 21
print((20-3) + 2 ** 2)


#### VARIABLES ####

#snake_case
score = 50

print (score)

#CONSTANTS
PI = 3.14

#dunder variables
#__main__

# assigning variables
a,b,c = 1,2,3

print (a)
print (b)
print (c)


# Expressions vs Statements
iq = 100 #statement
user_age = iq / 5 #expression produces a value

#augmented assignment operator
some_value = 5
some_value += 2

print(some_value)

#strings
username = 'supercoder'
long_string = '''
WOW
0 0
---
'''
print(long_string)
first_name = 'Romeo'
last_name = 'Enso'
full_name = first_name + ' ' + last_name
print(full_name)

#string concatenation
print('hello' + ' Romeo')

# cannot do a concatentation
# ---> print('hello' + 5)

#Type conversion
a = str(100)
b = int(a)
c = type(b)
print (c)

#Escape Sequence
status = 'It\'s \"kind of\" sunny'
print(status)

#Formatted strings
name = 'Arturito'
age = 55
print(f'hi {name}. You are {age} years old')

#string indexes
selfish = '01234567'
#          01234567

#SLICING = [start:stop:stepover]
#[-1] -> refers to the last index
#[::-1] -> reverses the array
print(selfish[::-1])

#Methods
quote = "to be or not to be"
print(quote.find('be'))
print(quote.replace('be', 'zzz'))

#Booleans
# True or False
#bool(0) = false
#bool(1) = true
#bool('True')
#bool('False')
name = "Romeo"
has_name = True
is_cool = False
print(f'Name: {name}, options: has_name: {has_name}, is_cool: {is_cool}')

#### Excercise: Type Conversion ####
birth_year = input("What year are you born?")
age = 2020 - int(birth_year)

print(f'''
Excercise:
You\'re age is now {age}
'''
)

#### Excercise: Password Checker ####
user_name = input('Username:')
pwd = input('Password:')
pwd_length = len(pwd)

print(f'''
Excercise: Password Checker
{user_name}, your password {'*' * pwd_length} is {pwd_length} letters long.
''')