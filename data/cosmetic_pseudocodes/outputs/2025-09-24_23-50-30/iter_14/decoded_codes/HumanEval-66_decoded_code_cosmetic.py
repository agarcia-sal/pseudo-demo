from typing import List


def digitSum(str_param: str) -> int:
    if str_param == "":
        return 0
    acc_list: List[int] = []
    for sym in str_param:
        if 'A' <= sym <= 'Z':
            acc_list.append(ord(sym))
        else:
            acc_list.append(0)
    total_val: int = sum(acc_list)
    return total_val