from typing import List


def all_prefixes(input_string: str) -> List[str]:
    def collector(accumulated_list: List[str], current_index: int) -> List[str]:
        if current_index >= len(input_string):
            return accumulated_list
        next_substring = input_string[:current_index + 1]
        return collector(accumulated_list + [next_substring], current_index + 1)
    return collector([], 0)