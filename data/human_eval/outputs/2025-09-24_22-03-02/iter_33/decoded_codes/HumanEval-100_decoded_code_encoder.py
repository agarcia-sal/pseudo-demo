def make_a_pile(n):
    result = []
    i = 0
    while i < n:
        value = n + 2 * i
        result.append(value)
        i += 1
    return result