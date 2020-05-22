class NameOfClass:
  class_attrs = 'value'

  def __init__(self, param1, param2):
    self.param1 = param1
    self.param2 = param2

  def method():
    #code

  @classmethod
  def class_method(cls, param1):
    #code

  @staticmethod
  def static_method(param2):
    #code

#OOP
class PlayerCharacter:
  #class attributes
  membersip = True #static

  #constructor
  def __init__(self, name="Bob", age=0):
    if (age >= 18):
      self.name = name #dynamic attributes
      self.age = age

  def shout(self):
    print(f'My name is {self.name}')

  # class method can be accessible by Class.method()
  # can also used by constructor
  @classmethod
  def adding_things(cls, n1, n2):
    return cls('Teddy', n1 + n2)

  #staticmethod -> no access cls
  @staticmethod
  def subtract(n2, n3):
    return n2 - n3

p1 = PlayerCharacter('Tom', 18)
print(p1)
print(p1.shout())
print(p1.adding_things(2,3))
p2 = PlayerCharacter.adding_things(34, 3)
print(p2.name)
# p2 = PlayerCharacter('Joy', 52)
# p2.attack = 40
# print(p2.name)
# print(p2)
# print(p2.attack)

