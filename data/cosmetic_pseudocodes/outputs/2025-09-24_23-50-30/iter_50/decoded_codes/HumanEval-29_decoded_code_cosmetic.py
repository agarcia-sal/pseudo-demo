from typing import List


def filter_by_prefix(arr_strings: List[str], str_prefix: str) -> List[str]:
    result_list: List[str] = []
    idx: int = 0

    while idx < len(arr_strings):
        current_item: str = arr_strings[idx]
        prefix_length: int = len(str_prefix)
        prefix_segment: str = current_item[:prefix_length]

        if prefix_segment == str_prefix:
            result_list.append(current_item)

        idx += 1

    return result_list