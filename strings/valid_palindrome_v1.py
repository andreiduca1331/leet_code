def isPalindrome(s: str) -> bool:
  alphabetic_letters = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "x", "y", "z"}
  digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
  s_alphanumeric = ""
  s_alphanumeric_reversed = ""
  for char in s:
    if char in digits:
      s_alphanumeric += char
      s_alphanumeric_reversed = char + s_alphanumeric_reversed
    if char.lower() in alphabetic_letters:
      s_alphanumeric += char.lower()
      s_alphanumeric_reversed = char.lower() + s_alphanumeric_reversed
  return s_alphanumeric == s_alphanumeric_reversed
