def is_happy(token: str) -> bool:
    if len(token) < 3:
        return False
    for pos in range(len(token) - 2):
        if token[pos] == token[pos + 1]:
            return False
        if token[pos + 1] == token[pos + 2]:
            return False
        if token[pos] == token[pos + 2]:
            return False
    return True