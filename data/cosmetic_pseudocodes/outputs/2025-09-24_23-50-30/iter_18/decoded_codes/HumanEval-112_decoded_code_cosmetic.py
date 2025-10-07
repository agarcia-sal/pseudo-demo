from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    result_arr: list[str] = [ch for ch in string_s if ch not in string_c]
    filtered_string: str = ''.join(result_arr)
    reversed_string: str = ''
    position: int = len(filtered_string) - 1
    while position >= 0:
        reversed_string += filtered_string[position]
        position -= 1
    return filtered_string, reversed_string == filtered_string