from typing import Sequence


def add(collection: Sequence[int]) -> int:
    def accumulate_even(index: int, total: int) -> int:
        if index > len(collection):
            return total
        current_element = collection[index - 1]  # 1-based to 0-based indexing
        if current_element % 2 == 0:
            total += current_element
        return accumulate_even(index + 2, total)

    return accumulate_even(1, 0)