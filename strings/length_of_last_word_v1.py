def lengthOfLastWord(s: str) -> int:
  if len(s) == 0:
    return 0
  right_index :int = len(s) - 1
  counter :int = 0
  while not s[right_index].isalnum() and right_index > 0:
    right_index -= 1
  while s[right_index].isalnum() and right_index >= 0:
    right_index -= 1
    counter += 1
  return counter

