#File Module

#open(name_file, 'mode')
# 'w', 'x', 'a', 'r'
# w -> write to the file
# a -> append to the file
# r -> read the file

open_file = open('basic.txt', 'w');

open_file.write('Hello \n');
open_file.write('Test \n');

open_file.close()

# Read a File
r_file = open('basic.txt', 'r')
# print(r_file.read())
# print(r_file.readline())

for c in r_file:
  print(c)


# Delete a File

import os

# os.remove('basic.txt')

# if file exist

if os.path.exists('basic.txt'):
  print('It exist')
else:
  print ('There is not such file')


#copy a file
from shutil import copyfile, move
copyfile('basic.txt', '2_basic.txt')

# rename and move a file
move('2_basic.txt', 'another_file.txt')