from typing import List


def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1

    counts: List[int] = [0] * (max(list_of_integers) + 1)

    def count_elements(pos: int) -> None:
        if pos >= len(list_of_integers):
            return
        counts[list_of_integers[pos]] += 1
        count_elements(pos + 1)

    count_elements(0)

    result: int = -1
    pointer: int = 1
    while pointer < len(counts):
        if not (counts[pointer] < pointer):
            result = pointer
        pointer += 1

    return result