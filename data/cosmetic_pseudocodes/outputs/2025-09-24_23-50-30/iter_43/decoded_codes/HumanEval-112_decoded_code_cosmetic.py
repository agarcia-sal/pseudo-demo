from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, str]:
    result_str = ''.join(ch for ch in string_s if ch not in string_c)
    reversed_str = result_str[::-1]
    return result_str, reversed_str