def get_positive(l: list) -> list:
    result = []
    for i in range(len(l)):
        e = l[i]
        if e > 0:
            result.append(e)
    return result