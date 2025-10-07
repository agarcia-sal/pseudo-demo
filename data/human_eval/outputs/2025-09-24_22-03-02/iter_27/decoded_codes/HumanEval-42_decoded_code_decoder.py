def incr_list(l: list) -> list:
    result = []
    index = 0
    while index < len(l):
        e = l[index]
        incremented_element = e + 1
        result.append(incremented_element)
        index += 1
    return result