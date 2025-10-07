from typing import List


def vowels_count(str_param: str) -> int:
    v_set: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    acc: int = 0
    idx: int = 0
    while idx < len(str_param):
        cond: bool = not (str_param[idx] not in v_set)
        acc += int(cond)
        idx += 1
    if str_param and (str_param[-1] == 'y' or str_param[-1] == 'Y'):
        acc += 1
    return acc