def incr_list(l: list) -> list:
    result = []
    for index in range(len(l)):
        element = l[index]
        incremented_element = element + 1
        result.append(incremented_element)
    return result