def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

# when creating a module

if __name__ == '__main__':
  # this will not be executed if imported
  print(add(10, 2))
  print(subtract(10, 2))
  print(multiply(10, 2))
  print(divide(10, 2))

