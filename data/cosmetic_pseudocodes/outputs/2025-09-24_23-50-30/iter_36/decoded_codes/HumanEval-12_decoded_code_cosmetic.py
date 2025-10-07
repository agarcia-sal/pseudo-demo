from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    def find_max_length(lst: List[str], current_max: int) -> int:
        if not lst:
            return current_max
        head, *tail = lst
        updated_max = max(len(head), current_max)
        return find_max_length(tail, updated_max)

    def locate_string_with_length(lst: List[str], target_length: int) -> Optional[str]:
        if not lst:
            return None
        head, *tail = lst
        if len(head) == target_length:
            return head
        return locate_string_with_length(tail, target_length)

    if not list_of_strings:
        return None

    max_len = find_max_length(list_of_strings[:], 0)
    return locate_string_with_length(list_of_strings[:], max_len)