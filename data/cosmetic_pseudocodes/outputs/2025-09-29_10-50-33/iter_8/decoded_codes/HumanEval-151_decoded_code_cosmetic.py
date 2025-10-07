from typing import Sequence


def double_the_difference(collection_of_values: Sequence[int | float]) -> int:
    def accumulate_sum(index: int, current_total: int) -> int:
        if index >= len(collection_of_values):
            return current_total
        element = collection_of_values[index]
        # Check conditions:
        # element > 0
        # element is odd (element % 2 != 0)
        # element's string representation does not contain '.'
        if not (element <= 0 or element % 2 == 0 or '.' in str(element)):
            return accumulate_sum(index + 1, current_total + element * element)
        else:
            return accumulate_sum(index + 1, current_total)

    return accumulate_sum(0, 0)