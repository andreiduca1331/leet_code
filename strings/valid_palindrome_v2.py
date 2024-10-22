def isPalindrome(s: str) -> bool:
  def is_alphanumeric(char: str) -> bool:
    alphabetic_letters = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "x", "y", "z"}
    digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    if char in alphabetic_letters or char in digits:
      return True
    return False
  left = 0
  right = len(s) - 1
  while left < right:
    foo = s[left]
    bar = s[right]
    if not is_alphanumeric(s[left].lower()):
      left += 1
    elif not is_alphanumeric(s[right].lower()):
      right -= 1
    elif s[left].lower() == s[right].lower():
      left += 1
      right -= 1
    else:
      return False

  return True
