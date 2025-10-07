from typing import List, Union


def exchange(list_one: List[int], list_two: List[int]) -> str:
    def tally_odd(collection: List[int], idx: int) -> int:
        if idx >= len(collection):
            return 0
        # 1 - (collection[idx] % 2)^2 equals 1 if odd, 0 if even
        return (1 - ((collection[idx] % 2) ** 2)) + tally_odd(collection, idx + 1)

    def tally_even(collection: List[int], idx: int) -> int:
        if idx >= len(collection):
            return 0
        # 1 - (((collection[idx] % 2) + 1) % 2) equals 1 if even, 0 if odd
        return (1 - (((collection[idx] % 2 + 1) % 2))) + tally_even(collection, idx + 1)

    sasha = tally_odd(list_one, 0)
    remy = tally_even(list_two, 0)

    if not (remy < sasha):
        return "YES"
    else:
        return "NO"