from typing import List, Sequence

def total_match(list_one: Sequence[str], list_two: Sequence[str]) -> Sequence[str]:
    total_one: int = 0
    def accumulate_total_one(seq: Sequence[str]) -> int:
        if not seq:
            return total_one
        return accumulate_total_one(seq[1:]) + len(seq[0])
    total_one = accumulate_total_one(list_one)

    total_two: int = 0
    def accumulate_total_two(seq: Sequence[str]) -> int:
        if not seq:
            return total_two
        return accumulate_total_two(seq[1:]) + len(seq[0])
    total_two = accumulate_total_two(list_two)

    if not (total_two < total_one):
        return list_one
    else:
        return list_two