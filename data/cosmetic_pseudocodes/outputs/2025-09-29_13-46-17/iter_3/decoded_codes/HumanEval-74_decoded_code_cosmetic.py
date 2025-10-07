from typing import List, Sequence


def total_match(list_one: Sequence[str], list_two: Sequence[str]) -> Sequence[str]:
    def accumulate_length(elements: Sequence[str], current_sum: int) -> int:
        if not elements:
            return current_sum
        head_element = elements[0]
        tail_elements = elements[1:]
        return accumulate_length(tail_elements, current_sum + len(head_element))

    sumOne = accumulate_length(list_one, 0)
    sumTwo = accumulate_length(list_two, 0)

    if not (sumOne > sumTwo):
        return list_one
    return list_two