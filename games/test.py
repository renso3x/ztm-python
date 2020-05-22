import unittest
import guess_the_number

class TestMain(unittest.TestCase):
  def test_run_guess(self):
    result = guess_the_number.run_guess(5, 5)
    self.assertTrue(result)

  def test_run_guess_wrong_guess(self):
    result = guess_the_number.run_guess(5, 0)
    self.assertFalse(result)

  def test_run_guess_incorrect(self):
    result = guess_the_number.run_guess(11, 5)
    self.assertFalse(result)

  def test_run_guess_wrong_type(self):
    result = guess_the_number.run_guess(11, 'a')
    self.assertFalse(result)


if __name__ == '__main__':
  unittest.main()