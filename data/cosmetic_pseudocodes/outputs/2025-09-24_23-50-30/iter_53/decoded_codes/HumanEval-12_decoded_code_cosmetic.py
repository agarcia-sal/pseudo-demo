from typing import List, Optional

def longest(array_of_entries: List[str]) -> Optional[str]:
    def identify_maximum(current_index: int, present_max: int) -> int:
        if current_index > len(array_of_entries):
            return present_max
        length_current = len(array_of_entries[current_index - 1])
        present_max = max(length_current, present_max)
        return identify_maximum(current_index + 1, present_max)

    def find_match(index_to_check: int, target_length: int) -> Optional[str]:
        if index_to_check > len(array_of_entries):
            return None
        if len(array_of_entries[index_to_check - 1]) == target_length:
            return array_of_entries[index_to_check - 1]
        return find_match(index_to_check + 1, target_length)

    if len(array_of_entries) == 0:
        return None
    max_len = identify_maximum(1, 0)
    return find_match(1, max_len)