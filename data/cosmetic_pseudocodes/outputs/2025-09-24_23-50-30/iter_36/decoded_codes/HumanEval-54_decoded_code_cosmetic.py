from typing import Set

def same_chars(str_a: str, str_b: str) -> bool:
    col_a: Set[str] = set()
    col_b: Set[str] = set()

    for idx_a in range(1, len(str_a) + 1):
        col_a.add(str_a[idx_a - 1])

    for idx_b in range(1, len(str_b) + 1):
        col_b.add(str_b[idx_b - 1])

    return col_a == col_b