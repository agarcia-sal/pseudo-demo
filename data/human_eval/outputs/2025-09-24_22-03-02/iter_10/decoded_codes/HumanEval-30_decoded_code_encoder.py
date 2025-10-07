def get_positive(l: list) -> list:
    result = []
    for e in l:
        if e > 0:
            result.append(e)
    return result