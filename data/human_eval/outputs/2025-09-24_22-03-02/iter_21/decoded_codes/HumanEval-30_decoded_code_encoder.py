def get_positive(l: list) -> list:
    result = []
    for index in range(len(l)):
        e = l[index]
        if e > 0:
            result.append(e)
    return result