from typing import Set

def same_chars(param_a: str, param_b: str) -> bool:
    temp_set_a: Set[str] = set()
    temp_set_b: Set[str] = set()

    index_i: int = 0
    while index_i < len(param_a):
        temp_set_a.add(param_a[index_i])
        index_i += 1

    index_i = 0
    while index_i < len(param_b):
        temp_set_b.add(param_b[index_i])
        index_i += 1

    return temp_set_a == temp_set_b