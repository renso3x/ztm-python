# Regular Expressions
import re

string = 'search inside of this teext please!'

match = re.search('this', string)

print(match.span())


# 8 char long
# contains any sort letters, numbers, $%#@
# end of a digit
pattern = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")
pwd = 'test12311'
checker = pattern.fullmatch(pwd)

print(checker)