from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    new_list: List[int] = []
    index: int = 0

    def add_one_rec(current_index: int) -> None:
        if current_index >= len(list_of_elements):
            return
        new_list.append(list_of_elements[current_index] + 1)
        add_one_rec(current_index + 1)

    add_one_rec(index)
    return new_list