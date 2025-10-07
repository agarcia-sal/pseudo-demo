from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars: list[str] = []

    def recursive_filter(index: int) -> None:
        if index >= len(string_s):
            return
        if string_s[index] not in string_c:
            filtered_chars.append(string_s[index])
        recursive_filter(index + 1)

    recursive_filter(0)
    filtered_string = ''.join(filtered_chars)
    return filtered_string, filtered_string == filtered_string[::-1]