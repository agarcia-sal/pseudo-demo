from typing import Set

def same_chars(string_p: str, string_q: str) -> bool:
    set_x: Set[str] = set()
    set_y: Set[str] = set()
    index_a: int = 0
    while index_a < len(string_p):
        set_x.add(string_p[index_a])
        index_a += 1
    index_b: int = 0
    while index_b < len(string_q):
        set_y.add(string_q[index_b])
        index_b += 1
    if set_x != set_y:
        return False
    else:
        return True