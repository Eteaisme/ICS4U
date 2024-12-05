def recExp(a,b):
    if b == 0: 
        return 1

    return a* recExp(a,b-1)

print(recExp(2,3))
