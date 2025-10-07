def digitSum(str_val: str) -> int:
    acc_num: int = 0
    idx: int = 0
    while idx < len(str_val):
        sym: str = str_val[idx]
        if 'A' <= sym <= 'Z':
            code: int = ord(sym)
            acc_num += code
        else:
            acc_num += 0
        idx += 1
    return acc_num