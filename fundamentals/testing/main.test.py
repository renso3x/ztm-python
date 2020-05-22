import unittest
from main import add

class TestMain(unittest.TestCase):
  #run before a functon
  def setUp(self):
    print('about to test a function')

  def test_add_if_variable_is_string(self):
    num = 'aaaå'
    result = add(num)
    self.assertIsInstance(result, ValueError)

  def test_add_should_return_sum(self):
    num = 10
    result = add(num)
    self.assertEqual(result, 15)

  def test_add_if_none_type(self):
    num = None
    result = add(num)
    self.assertEqual(result, 'please enter a number')

  def test_add_if_empty_str(self):
    num = ''
    result = add(num)
    self.assertEqual(result, 'please enter a number')

  #run after every function
  #good to clear databases
  def tearDown(self):
    print('cleaning up')

#only run this file if this is run
if __name__ == '__main__':
  unittest.main()


