def incr_list(l: list) -> list:
    result = []
    index = 0
    while index < len(l):
        e = l[index]
        incremented_value = e + 1
        result.append(incremented_value)
        index += 1
    return result