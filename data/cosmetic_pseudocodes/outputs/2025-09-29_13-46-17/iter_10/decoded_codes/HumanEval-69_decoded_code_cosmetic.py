from typing import List


def search(list_of_integers: List[int]) -> int:
    max_val: int = max(list_of_integers, default=0) + 1
    counts: List[int] = [0] * max_val

    # Count occurrences of each integer in list_of_integers
    for num in list_of_integers:
        # Only increment if num is within [0, max_val)
        if 0 <= num < max_val:
            counts[num] += 1

    result: int = -1

    def loop(idx: int) -> int:
        nonlocal result
        if idx == max_val:
            return result
        count_at_idx = counts[idx]
        if not (count_at_idx < idx):
            result = idx
        return loop(idx + 1)

    return loop(1)