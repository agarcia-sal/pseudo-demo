def is_happy(str_param: str) -> bool:
    if len(str_param) < 3:
        return False
    limit = len(str_param) - 3
    pos = 0
    while pos <= limit:
        a, b, c = str_param[pos], str_param[pos + 1], str_param[pos + 2]
        if a == b or b == c or a == c:
            return False
        pos += 1
    return True