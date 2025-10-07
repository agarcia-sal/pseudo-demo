def get_positive(l: list):
    result = []
    index = 0
    while index < len(l):
        e = l[index]
        if e > 0:
            result.append(e)
        index += 1
    return result