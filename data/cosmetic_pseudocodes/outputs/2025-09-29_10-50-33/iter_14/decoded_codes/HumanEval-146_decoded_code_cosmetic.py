from typing import Sequence


def specialFilter(collection_of_values: Sequence[int]) -> int:
    tally: int = 0
    odd_set = {9, 1, 7, 3, 5}

    def recursiveCheck(position: int) -> None:
        nonlocal tally
        if position > len(collection_of_values):
            return
        current_element = collection_of_values[position - 1]  # 1-based to 0-based index
        if current_element > 10:
            string_form = str(current_element)
            if (int(string_form[0]) in odd_set and int(string_form[-1]) in odd_set):
                tally += 1
        recursiveCheck(position + 1)

    recursiveCheck(1)
    return tally