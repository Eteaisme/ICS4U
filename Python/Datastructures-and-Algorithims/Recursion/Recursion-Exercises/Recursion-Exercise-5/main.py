def sumDigits(n):
    if n == 0:
        return 0
    return (n % 10) + sumDigits(n // 10)

print(sumDigits(123))
