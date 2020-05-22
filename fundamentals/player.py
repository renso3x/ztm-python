# OOP 4 pillars
# 1.Encapsulation - scope of variables
# 2.Abstraction - hide away implementation, just share the needed attributes, methods. Can have a private and public. No private variables in python, but you can use _ to achieve privacy
# 3. Inheritance - take inherit from classes
# 4. Polymorphism - can inherit a method, but can act ina different behavior, can be customizable, ovveriding a method from the base class, ability to redefine methods

class Player():
  # dunder method is build-in methods
  def __init__(self, name, age = 0):
    self._name = name
    self._age = age

  def speak(self):
    print(f'My name is {self._name} and my age is {self._age}')

p1 = Player('Romeo', 24)
p1.speak()

# INHERTIANCE Example

#BASE CLASS
class User():
  # def __init__(self, email):
  #   self.email = email

  def sign_in(self):
    print('logging in')

#SUB CLASS
class Wizard(User):
  def __init__(self, name, power, email):
    #super call -> refers to the user class
    #super().__init__(email)
    self.name = name
    self.power = power

  def attack(self):
    print(f'attaching power {self.power}')

class Archer(User):
  def __init__(self, name, arrows):
    self.name = name
    self.arrows = arrows

  def check_arrow(self):
    print(f'arrows lef {self.arrows}')

  def attack(self):
    print ('Archer attacking')

  def run(self):
    print('ran really')

w = Wizard('Romeo', 5000, 'romek@gmail.com')
#introspection -> dir(), help()
print(dir(w)) #gives you the available method, attributes
w.sign_in()
w.attack()
print(isinstance(w, Wizard))

a = Archer('Legolaz', 12000)
a.check_arrow()
a.sign_in()

def player_attack(char):
  char.attack()

player_attack(w)
player_attack(a)

#dunder method
class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age

  #modifying dunder method
  def __str__(self):
    return f'{self.color}'

action_fig = Toy('red', 3)
print(str(action_fig))
print(action_fig.__str__())

# Excercise
# extend from the list
class SuperList(list):
  def __len__(self):
    return 1000

super_list = SuperList()

print(len(super_list))
print(super_list.append(5))
print(super_list[0])

print(issubclass(SuperList, list))