from unittest import TestCase

from strings.valid_palindrome_solution_v2 import isPalindrome

class TestSolution(TestCase):

  # def test_only_numbers(self):
  #   self.assertTrue(isPalindrome("12321"))

  # def test_only_letters(self):
  #   self.assertTrue(isPalindrome("racecar"))

  # def test_mixed_case(self):
  #   self.assertTrue(isPalindrome("12racecar21"))

  # def test_empty_string(self):
  #   self.assertTrue(isPalindrome(""))

  # def test_special_characters(self):
  #   self.assertTrue(isPalindrome("@#$%^&*()"))

  # def test_not_palindrome(self):
  #   self.assertFalse(isPalindrome("hello world"))

  # def test_not_palindrome_mixed_case(self):
  #   self.assertFalse(isPalindrome(",,,,,,,,,,,,acva"))

  def test_is_palindrome(self):
    self.assertTrue(isPalindrome("A man, a plan, a canal: Panama"))