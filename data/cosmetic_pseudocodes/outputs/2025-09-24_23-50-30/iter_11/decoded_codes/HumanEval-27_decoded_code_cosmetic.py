from typing import List

def flip_case(str_arg: str) -> str:
    res_array: List[str] = []
    idx: int = 0
    while idx < len(str_arg):
        c = str_arg[idx]
        if c == c.lower():
            res_array.append(c.upper())
        else:
            res_array.append(c.lower())
        idx += 1
    return ''.join(res_array)