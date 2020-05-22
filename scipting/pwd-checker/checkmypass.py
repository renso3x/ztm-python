#use pwnedpasswords

import requests
import hashlib
import sys

def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  print(url)
  res = requests.get(url)

  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, please try again.')

  return res

def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    #check if the tail of our hash
    if h == hash_to_check:
      return count

  return 0

def pwned_api_check(password):
  #check password if it exist in API response
  #convert the password to hash
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first_five_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first_five_char)

  return get_password_leaks_count(response, tail)

def main(args):
  for pwd in args:
    count = pwned_api_check(pwd)
    if count:
      print(f'{pwd} was found {count} times... you should probably change your password')
    else:
      print(f'{pwd} was not found {count}. Carry on!')
  return 'done!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))

