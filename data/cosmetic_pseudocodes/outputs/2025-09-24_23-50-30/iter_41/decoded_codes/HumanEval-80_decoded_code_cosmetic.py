from typing import Sequence, Any

def is_happy(param_one: Sequence[Any]) -> bool:
    if len(param_one) < 3:
        return False
    max_val = len(param_one) - 3
    start_val = 0
    while start_val <= max_val:
        a = param_one[start_val]
        b = param_one[start_val + 1]
        c = param_one[start_val + 2]
        if not (a != b and b != c and a != c):
            return False
        start_val += 1
    return True