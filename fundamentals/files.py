# Script for read, write, append
# Excercise read from a file
# add translation
# create a new file for the translation
from translate import Translator

translator = Translator(to_lang="ja")

try:
  with open('another_file.txt', mode="r") as my_file:
    text = my_file.read()
    translation = translator.translate(text)

    with open('translate-file.txt', mode="w") as my_new:
      my_new = my_new.write(translation)
except FileNotFoundError:
  print('Check your file')



#File Paths
