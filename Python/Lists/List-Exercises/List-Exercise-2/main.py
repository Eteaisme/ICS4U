def is_descending(array):
  if len(array) == 1:
    return True
  if(array[0] < array[1]):
    return False
  return is_descending(array[1:])

print(is_descending([20,19,16,9,3,1,0])) #True
print(is_descending([36,29,57,16,12,4,3])) #False