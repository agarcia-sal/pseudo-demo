from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    def find_max_length(strings_iter: List[str], current_max: int) -> int:
        if not strings_iter:
            return current_max
        head_element = strings_iter[0]
        tail_elements = strings_iter[1:]
        head_length = len(head_element)
        updated_max = head_length if head_length > current_max else current_max
        return find_max_length(tail_elements, updated_max)

    def locate_longest_string(strings_iter: List[str], target_length: int) -> Optional[str]:
        if not strings_iter:
            return None
        candidate_string = strings_iter[0]
        remainder_list = strings_iter[1:]
        if len(candidate_string) == target_length:
            return candidate_string
        return locate_longest_string(remainder_list, target_length)

    if not list_of_strings:
        return None
    max_len = find_max_length(list_of_strings, -1)
    return locate_longest_string(list_of_strings, max_len)