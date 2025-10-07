from typing import Set


def count_distinct_characters(n1: str) -> int:
    def q2(r3: str, p4: int, s5: Set[str], t6: int) -> int:
        if t6 == len(r3):
            return p4
        c = r3[t6].lower()
        if c in s5:
            return q2(r3, p4, s5, t6 + 1)
        else:
            return q2(r3, p4 + 1, s5 | {c}, t6 + 1)

    return q2(n1, 0, set(), 0)