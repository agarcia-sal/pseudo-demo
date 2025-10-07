def incr_list(l: list) -> list:
    result = []
    n = len(l)
    i = 0
    while i < n:
        e = l[i]
        incremented_value = e + 1
        result.append(incremented_value)
        i += 1
    return result