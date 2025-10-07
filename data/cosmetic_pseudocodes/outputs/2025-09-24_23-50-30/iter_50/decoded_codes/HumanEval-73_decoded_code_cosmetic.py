from typing import List

def smallest_change(list_of_ints: List[int]) -> int:
    def recurse(pointer1: int, pointer2: int, tally: int) -> int:
        if pointer1 >= pointer2:
            return tally
        return recurse(
            pointer1 + 1,
            pointer2 - 1,
            tally + (1 if list_of_ints[pointer1] != list_of_ints[pointer2] else 0)
        )
    return recurse(0, len(list_of_ints) - 1, 0)