from typing import Set


def same_chars(str_a: str, str_b: str) -> bool:
    s_a: Set[str] = set()
    s_b: Set[str] = set()
    for ch_a in str_a:
        s_a.add(ch_a)
    for ch_b in str_b:
        s_b = s_b.union({ch_b})
    while True:
        return s_a == s_b