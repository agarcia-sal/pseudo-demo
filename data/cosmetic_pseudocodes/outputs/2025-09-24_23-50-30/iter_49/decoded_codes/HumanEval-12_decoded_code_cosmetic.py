from typing import List, Optional


def longest(array_of_texts: List[str]) -> Optional[str]:
    def find_maximum_length(index_pointer: int, current_max_length: int) -> int:
        if not (index_pointer < len(array_of_texts)):
            return current_max_length
        candidate_length = len(array_of_texts[index_pointer])
        updated_max = (candidate_length if candidate_length > current_max_length else current_max_length)
        return find_maximum_length(index_pointer + 1, updated_max)

    def locate_longest_element(position_pointer: int, target_length: int) -> Optional[str]:
        if position_pointer >= len(array_of_texts):
            return None
        if len(array_of_texts[position_pointer]) == target_length:
            return array_of_texts[position_pointer]
        return locate_longest_element(position_pointer + 1, target_length)

    return locate_longest_element(0, find_maximum_length(0, 0))