from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def filter_chars(input_str: str, removal_str: str, idx: int) -> str:
        if idx >= len(input_str):
            return ""
        current_char = input_str[idx]
        tail_filtered = filter_chars(input_str, removal_str, idx + 1)
        if current_char not in removal_str:
            return current_char + tail_filtered
        return tail_filtered

    filtered_str = filter_chars(string_s, string_c, 0)

    def is_palindrome(check_str: str, left_idx: int, right_idx: int) -> bool:
        while left_idx < right_idx:
            if check_str[left_idx] != check_str[right_idx]:
                return False
            left_idx += 1
            right_idx -= 1
        return True

    palindrome_result = is_palindrome(filtered_str, 0, len(filtered_str) - 1)

    return filtered_str, palindrome_result