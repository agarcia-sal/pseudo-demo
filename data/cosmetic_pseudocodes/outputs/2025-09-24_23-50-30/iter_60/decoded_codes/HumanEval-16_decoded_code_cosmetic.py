from typing import Set


def count_distinct_characters(p: str, q: str, r: Set[str]) -> int:
    r.clear()

    def process(i: int) -> None:
        if i == len(p):
            return
        ch = p[i].lower()
        r.add(ch)
        process(i + 1)

    process(0)
    return len(r)