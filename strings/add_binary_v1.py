def addBinary(s: str, t: str) -> str:
  def bytes_to_sum(input_str: str) -> int:
    if len(input_str) < 1:
      raise ValueError("Empty string provided!")
    expected_values = [0,1]
    right_index = len(input_str) - 1
    left_index = 0
    sum = 0
    while right_index >= 0:
      if not int(input_str[right_index]) in expected_values:
        raise ValueError("Expected only 0s or 1s!")
      sum += int(input_str[right_index]) * 2 ** left_index
      right_index -= 1
      left_index += 1
    return sum
  def num_to_bytes(num:int) -> str:
    if num == 0:
      return "0"
    result = ""
    while int(num / 2) > 0 or int(num % 2) != 0:
      result = str(int(num % 2)) + result
      num /= 2
    return result
  return num_to_bytes(bytes_to_sum(s) + bytes_to_sum(t))

