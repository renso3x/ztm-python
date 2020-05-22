#dont consume in memory
def generator_func(num):
  for i in range(num):
      yield i

g = generator_func(3)
# next(g)
# next(g)
# print(next(g))

# Under the hood Array
def special_for(iterable):
  iterable = iter(iterable)

  while True:
    try:
      print(iterable)
      print(next(iterable))
    except StopIteration:
      break

# special_for([1,2,3])


#Range
class MyGen():

  current = 0

  def __init__(self, first, last):
    self.first = first
    self.last = last

  def __iter__(self):
    return self

  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration

# gen = MyGen(0, 100)
# for i in gen:
#   print(i)


# Excercise: Fibonnacci
def fib(number):
  a = 0 #starting variable
  b = 1
  for i in range(number):
    yield a
    temp = a # holds the number of before swapping the value of a
    a = b
    b = temp + b


for x in fib(10000):
  print(x)



def fib2(number):
  a = 0
  b = 1
  result = []
  for i in range(number):
    result.append(a)
    temp = a # holds the number of before swapping the value of a
    a = b
    b = temp + b

  return result

# print(fib2(10000))

