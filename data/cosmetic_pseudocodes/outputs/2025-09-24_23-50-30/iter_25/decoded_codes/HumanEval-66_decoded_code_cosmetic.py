def digitSum(str_param: str) -> int:
    if not (str_param != ""):
        return 0
    acc_total: int = 0
    for ch in str_param:
        if 'A' <= ch <= 'Z':
            acc_total += ord(ch)
        else:
            acc_total += 0
    return acc_total