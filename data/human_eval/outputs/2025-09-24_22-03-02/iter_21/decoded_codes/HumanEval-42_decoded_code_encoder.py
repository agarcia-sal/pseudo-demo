def incr_list(l: list) -> list:
    result = []
    for index in range(len(l)):
        e = l[index]
        incremented = e + 1
        result.append(incremented)
    return result