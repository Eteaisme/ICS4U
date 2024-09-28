def is_descending(array):
  if len(array) <= 1:
    return True
  if(array[0] < array[1]):
    return False
  return is_descending(array[1:])

