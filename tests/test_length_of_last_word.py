from unittest import TestCase

from strings.length_of_last_word_v1 import lengthOfLastWord

class LengthOfLastWord(TestCase):

  def test_length_of_last_word(self):
    s = "Hello World"
    result = lengthOfLastWord(s)
    expected = len("World")
    self.assertEqual(result, expected)

  def test_empty_string(self):
    s = ""
    result = lengthOfLastWord(s)
    expected = 0
    self.assertEqual(result, expected)

  def test_with_multiple_spaces(self):
    s = "Hello    World"
    result = lengthOfLastWord(s)
    expected = len("World")
    self.assertEqual(result, expected)

  def test_with_no_spaces(self):
    s = "Hello"
    result = lengthOfLastWord(s)
    expected = len("Hello")
    self.assertEqual(result, expected)

  def test_with_whitespace_at_end(self):
    s = "Hello "
    result = lengthOfLastWord(s)
    expected = len("Hello")
    self.assertEqual(result, expected)