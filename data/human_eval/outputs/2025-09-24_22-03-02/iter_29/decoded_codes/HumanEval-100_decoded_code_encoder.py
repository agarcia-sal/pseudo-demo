def make_a_pile(n):
    result = []
    for i in range(n):
        stone_count = n + 2 * i
        result.append(stone_count)
    return result