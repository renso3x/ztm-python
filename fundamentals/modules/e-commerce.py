# 2 ways to import in python
# import package.module
# from package.modue import function/method
from shopping.cart import buy

if __name__ == '__main__':
  shirt = "red shirt"

  new_cart = buy(shirt)

  print(new_cart)