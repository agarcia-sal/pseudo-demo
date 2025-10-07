from typing import List

def vowels_count(str_param: str) -> int:
    container: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    acc_var: int = 0
    idx_var: int = 0
    while idx_var < len(str_param):
        if str_param[idx_var] in container:
            acc_var += 1
        idx_var += 1
    if str_param and str_param[-1] in ('Y', 'y'):
        acc_var += 1
    return acc_var