def count_upper(str_param: str) -> int:
    acc: int = 0
    pos: int = 0
    while pos < len(str_param):
        if str_param[pos] in "AEIOU":
            acc += 1
        pos += 2
    return acc