def incr_list(l: list) -> list:
    result = []
    index = 0
    while index < len(l):
        e = l[index]
        incremented = e + 1
        result.append(incremented)
        index += 1
    return result