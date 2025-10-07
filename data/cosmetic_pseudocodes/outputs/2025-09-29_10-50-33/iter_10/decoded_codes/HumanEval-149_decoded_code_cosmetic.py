from typing import List

def sorted_list_sum(list_of_strings: List[str]) -> List[str]:
    accumulator: List[str] = []

    def iterate(index: int) -> None:
        if index >= len(list_of_strings):
            return
        current_item = list_of_strings[index]
        if len(current_item) % 2 == 0:
            accumulator.append(current_item)
        iterate(index + 1)

    iterate(0)
    return sorted(accumulator, key=len)