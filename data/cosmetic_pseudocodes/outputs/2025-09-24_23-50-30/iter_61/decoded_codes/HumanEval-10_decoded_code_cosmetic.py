from typing import List


def is_palindrome(alpha: str) -> bool:
    return recur_is_palindrome(0, len(alpha) - 1, alpha)


def recur_is_palindrome(left_idx: int, right_idx: int, alpha: str) -> bool:
    while True:
        if left_idx >= right_idx:
            return True
        if alpha[left_idx] != alpha[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1


def make_palindrome(input_str: str) -> str:
    def search_prefix(idx: int, s: str) -> int:
        if idx >= len(s):
            return idx
        if is_palindrome(s[idx:]):
            return idx
        return search_prefix(idx + 1, s)

    if len(input_str) == 0:
        return ""
    prefix_marker = search_prefix(0, input_str)
    # Append reverse of the substring before prefix_marker
    return input_str + input_str[:prefix_marker][::-1]