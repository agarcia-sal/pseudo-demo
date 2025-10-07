from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    def helper(index: int, acc: List[str]) -> List[str]:
        if index == len(list_of_strings):
            return acc
        current_str = list_of_strings[index]
        if current_str.startswith(prefix_string):
            return helper(index + 1, acc + [current_str])
        else:
            return helper(index + 1, acc)
    return helper(0, [])