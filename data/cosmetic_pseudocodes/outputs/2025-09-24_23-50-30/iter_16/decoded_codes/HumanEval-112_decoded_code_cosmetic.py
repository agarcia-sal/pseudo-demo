from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def filter_chars(chars: str, forbidden_chars: str, index: int, acc: str) -> str:
        if index >= len(chars):
            return acc
        if chars[index] not in forbidden_chars:
            return filter_chars(chars, forbidden_chars, index + 1, acc + chars[index])
        else:
            return filter_chars(chars, forbidden_chars, index + 1, acc)

    filtered_str = filter_chars(string_s, string_c, 0, "")
    reversed_str = "".join(filtered_str[i] for i in range(len(filtered_str) - 1, -1, -1))
    return filtered_str, reversed_str == filtered_str