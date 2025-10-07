from typing import List, Iterator

def get_positive(list_of_numbers: List[int]) -> List[int]:
    filtered_numbers: List[int] = []
    iterator: Iterator[int] = iter(list_of_numbers)

    def accumulate_positive() -> None:
        try:
            current_item = next(iterator)
        except StopIteration:
            return
        if current_item > 0:
            filtered_numbers.append(current_item)
        accumulate_positive()

    accumulate_positive()
    return filtered_numbers