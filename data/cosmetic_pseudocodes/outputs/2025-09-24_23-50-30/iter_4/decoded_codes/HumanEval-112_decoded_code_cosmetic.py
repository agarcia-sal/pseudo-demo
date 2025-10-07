from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def filtered_chars(index: int, acc: str) -> str:
        if index >= len(string_s):
            return acc
        if string_s[index] not in string_c:
            return filtered_chars(index + 1, acc + string_s[index])
        return filtered_chars(index + 1, acc)

    result_str = filtered_chars(0, "")
    is_palindrome = result_str == result_str[::-1]
    return result_str, is_palindrome