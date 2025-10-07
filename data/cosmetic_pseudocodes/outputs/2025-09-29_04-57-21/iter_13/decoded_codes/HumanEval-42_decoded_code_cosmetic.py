from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    updated_elements: List[int] = []

    def recursive_incrementer(index: int) -> None:
        if index == len(list_of_elements):
            return
        updated_elements.append(1 + list_of_elements[index])
        recursive_incrementer(index + 1)

    recursive_incrementer(0)
    return updated_elements