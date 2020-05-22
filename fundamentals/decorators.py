#Decorator Pattern => High Order Component
def my_decorator(func):
  def wrap_func(*args, **kwargs):
    print('******')
    func(*args, **kwargs)
    print('******')
  return wrap_func

@my_decorator
def hello(*args, **kwargs):
  print(*args)
  print(kwargs["name"], kwargs["age"])

hello('saaddd', name="romeo", age=26)



from time import time

def perfomance(fn):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = fn(*args, ** kwargs)
    t2 = time()
    print(f'It took {t2-t1} s')
    return result
  return wrapper

@perfomance
def long_time():
  # faster since this is a generator
  for i in range(10000):
    i * 5

@perfomance
def long_time2():
  for i in list(range(10000)):
    i*5

long_time()
long_time2()