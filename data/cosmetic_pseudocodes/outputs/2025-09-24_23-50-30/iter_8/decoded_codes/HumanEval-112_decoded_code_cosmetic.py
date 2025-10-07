from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    result_chars: list[str] = [ch for ch in string_s if ch not in string_c]
    filtered_string: str = "".join(result_chars)

    pointer_front: int = 0
    pointer_back: int = len(filtered_string) - 1
    palindrome_flag: bool = True

    while pointer_front < pointer_back and palindrome_flag:
        if filtered_string[pointer_front] != filtered_string[pointer_back]:
            palindrome_flag = False
        pointer_front += 1
        pointer_back -= 1

    return filtered_string, palindrome_flag