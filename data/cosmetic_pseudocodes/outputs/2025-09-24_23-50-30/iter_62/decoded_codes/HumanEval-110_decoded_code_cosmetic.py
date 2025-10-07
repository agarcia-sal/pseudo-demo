from typing import Sequence


def exchange(collection_alpha: Sequence[int], collection_beta: Sequence[int]) -> str:
    def tally_odd(items: Sequence[int], idx: int, tally: int) -> int:
        if idx >= len(items):
            return tally
        if items[idx] % 2 == 1:
            return tally_odd(items, idx + 1, tally + 1)
        return tally_odd(items, idx + 1, tally)

    def tally_even(items: Sequence[int], idx: int, tally: int) -> int:
        if idx >= len(items):
            return tally
        if items[idx] % 2 == 0:
            return tally_even(items, idx + 1, tally + 1)
        return tally_even(items, idx + 1, tally)

    count_odd = tally_odd(collection_alpha, 0, 0)
    count_even = tally_even(collection_beta, 0, 0)

    return "YES" if not (count_even < count_odd) else "NO"