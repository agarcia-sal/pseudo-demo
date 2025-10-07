def make_a_pile(n):
    result = []
    for i in range(n):
        stones = n + 2 * i
        result.append(stones)
    return result