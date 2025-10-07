from typing import List


def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    def compute_length(strs: List[str], idx: int, acc: int) -> int:
        if idx >= len(strs):
            return acc
        else:
            return compute_length(strs, idx + 1, acc + len(strs[idx]))

    len_a = compute_length(list_one, 0, 0)
    len_b = compute_length(list_two, 0, 0)

    if not (len_a > len_b):
        return list_one
    return list_two