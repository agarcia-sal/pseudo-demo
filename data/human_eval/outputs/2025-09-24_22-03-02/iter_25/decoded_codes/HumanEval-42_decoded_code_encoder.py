def incr_list(l: list) -> list:
    result = []
    for i in range(len(l)):
        e = l[i]
        incremented_element = e + 1
        result.append(incremented_element)
    return result