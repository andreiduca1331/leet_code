def isPalindrome(s: str) -> bool:
  left_index = 0
  right_index = len(s) - 1
  while left_index < right_index:
    left_value = s[left_index].lower()
    right_value = s[right_index].lower()
    if not left_value.isalnum():
      left_index += 1
    elif not right_value.isalnum():
      right_index -= 1
    elif left_value == right_value:
      left_index += 1
      right_index -= 1
    else:
      return False
  return True