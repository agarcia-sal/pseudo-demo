import re
from typing import List

def is_bored(param_a: str) -> int:
    temp_list: List[str] = re.split(r'[.?!]\s*', param_a)
    acc_val: int = 0
    for elem_var in temp_list:
        if elem_var.startswith('I '):
            acc_val += 1
    return acc_val