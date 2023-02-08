def sum_in_range(min, max):
  sum = 0
  for x in range(min, max):
    sum += x
  return sum


result = sum_in_range(7, 69)
print(result)
print(sum_in_range(1, 11))
print(sum_in_range(result, result + 69))
