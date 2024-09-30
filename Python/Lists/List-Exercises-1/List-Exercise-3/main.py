def fibonacci(n):
    if n <= 2:
        return [0, 1][:n]
    array = fibonacci(n-1)
    return array + [array[-1] + array[-2]]

print(fibonacci(8))
print(fibonacci(12))
print(fibonacci(24))