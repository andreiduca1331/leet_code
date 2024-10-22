from unittest import TestCase

from strings.add_binary_v1 import addBinary

class AddBinary(TestCase):
  def test_add_binary(self):
    s = "11"
    t = "1"
    result = addBinary(s, t)
    expected = "100"
    self.assertEqual(result, expected)

  def test_add_binary_2(self):
    s = "1010"
    t = "1011"
    result = addBinary(s, t)
    expected = "10101"
    self.assertEqual(result, expected)

  def test_add_binary_with_zero(self):
    s = "11"
    t = "0"
    result = addBinary(s, t)
    expected = "11"
    self.assertEqual(result, expected)

  def test_add_binary_with_zero_2(self):
    s = "0"
    t = "0"
    result = addBinary(s, t)
    expected = "0"
    self.assertEqual(result, expected)

  def test_invalid_input(self):
    s = "11"
    t = "2"
    with self.assertRaises(ValueError):
      addBinary(s, t)

  def test_invalid_input_2(self):
    s = "11"
    t = "a"
    with self.assertRaises(ValueError):
      addBinary(s, t)