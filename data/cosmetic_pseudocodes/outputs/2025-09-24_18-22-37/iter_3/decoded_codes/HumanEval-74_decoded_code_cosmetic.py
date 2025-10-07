from typing import List, Sequence

def total_match(list_one: Sequence[str], list_two: Sequence[str]) -> List[str]:
    def sum_lengths(items: Sequence[str], idx: int, acc: int) -> int:
        if idx >= len(items):
            return acc
        return sum_lengths(items, idx + 1, acc + len(items[idx]))

    total_one = sum_lengths(list_one, 0, 0)
    total_two = sum_lengths(list_two, 0, 0)

    if total_one <= total_two:
        return list(list_one)
    return list(list_two)