from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    result_list: list[str] = []
    index_i: int = 0
    while index_i < len(string_s):
        if string_s[index_i] not in string_c:
            result_list.append(string_s[index_i])
        index_i += 1
    filtered_str: str = "".join(result_list)
    reversed_str: str = ""
    pos_j: int = len(filtered_str) - 1
    while pos_j >= 0:
        reversed_str += filtered_str[pos_j]
        pos_j -= 1
    return filtered_str, reversed_str == filtered_str