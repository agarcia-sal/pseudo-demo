from typing import List


def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    filtered_list: List[str] = []

    def helper(index: int) -> None:
        if index < len(list_of_strings):
            if list_of_strings[index].startswith(prefix_string):
                filtered_list.append(list_of_strings[index])
            helper(index + 1)

    helper(0)
    return filtered_list