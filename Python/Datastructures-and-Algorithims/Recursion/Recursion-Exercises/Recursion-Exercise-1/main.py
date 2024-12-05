def addUp(a1):
    if len(a1) == 1:
        return a1[0]
    return a1[0] + addUp(a1[1:])

arr = [1,2,3,4,5,6,7,8,9]

print(addUp(arr))