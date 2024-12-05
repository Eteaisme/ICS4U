def hanoiMoves(n):
    if n == 0:
        return 0
    return 2 * hanoiMoves(n - 1) + 1

print(hanoiMoves(5))
