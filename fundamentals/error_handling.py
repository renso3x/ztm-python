#Error handling

while True:
  try:
    age = int(input('what is your age?'))
    # print(age)
    # what if like this 10/age
    10/age
  except ValueError: #can except an error type
    print("please enter a number")
    continue
  except ZeroDivisionError:
    print("please enter age higher than 0")
    break
  else:
    print('thank you')
    # print something or other operation
    break
  finally: #always fires after the try except
    print('ok, i am finally done')

def sum(num1, num2):
  try:
    return num1/num2
  except (TypeError, ZeroDivisionError) as err:
    print(f'{err}')

print(sum(0, 2))