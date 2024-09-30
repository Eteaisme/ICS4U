def remove_duplicates(array):
    if not array:
        return []
    firstElement = array[0] 
    remainingElements = array[1:]
    newArray = remove_duplicates([i for i in remainingElements if i != firstElement])
    
    return [firstElement] + newArray


print (remove_duplicates([1, 2, 3, 3, 4, 8, 8, 9, 5, 2, 1, 5]))