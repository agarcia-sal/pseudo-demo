from typing import Sequence, Union

def same_chars(param_a: Union[str, Sequence[str]], param_b: Union[str, Sequence[str]]) -> bool:
    temp_set1: set[str] = set()
    temp_set2: set[str] = set()

    idx_a = 0
    len_a = len(param_a)
    while idx_a < len_a:
        current_char = param_a[idx_a]
        temp_set1.add(current_char)
        idx_a += 1

    idx_b = 0
    len_b = len(param_b)
    while idx_b < len_b:
        current_char = param_b[idx_b]
        temp_set2.add(current_char)
        idx_b += 1

    return temp_set1 == temp_set2