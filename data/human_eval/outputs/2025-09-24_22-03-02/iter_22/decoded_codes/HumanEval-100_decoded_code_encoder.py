def make_a_pile(n):
    result = []
    i = 0
    while i < n:
        stones = n + 2 * i
        result.append(stones)
        i += 1
    return result