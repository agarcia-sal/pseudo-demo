def make_a_pile(n):
    result = []
    i = 0
    while i < n:
        current_value = n + 2 * i
        result.append(current_value)
        i += 1
    return result