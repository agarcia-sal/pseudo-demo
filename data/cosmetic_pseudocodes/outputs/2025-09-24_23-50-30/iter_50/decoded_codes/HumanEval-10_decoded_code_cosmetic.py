from typing import List


def is_palindrome(input_string: str) -> bool:
    def reverse_eq_check(s: str) -> bool:
        def reverse_chars(lst: List[str], idx: int, end: int) -> List[str]:
            if idx >= end:
                return []
            return reverse_chars(lst, idx + 1, end) + [lst[idx]]

        char_list = list(s)
        reversed_list = reverse_chars(char_list, 0, len(char_list))
        return char_list == reversed_list

    return reverse_eq_check(input_string)


def make_palindrome(input_string: str) -> str:
    def find_pal_prefix(pos: int) -> int:
        if pos > len(input_string):
            return pos
        rem_substring = input_string[pos:]
        if not is_palindrome(rem_substring):
            return find_pal_prefix(pos + 1)
        else:
            return pos

    if len(input_string) == 0:
        return ""

    start_index = find_pal_prefix(0)
    front_part = input_string[:start_index]

    def reverse_list(lst: List[str], idx: int, acc: List[str]) -> List[str]:
        if idx < 0:
            return acc
        return reverse_list(lst, idx - 1, acc + [lst[idx]])

    reversed_front = "".join(reverse_list(list(front_part), len(front_part) - 1, []))
    return input_string + reversed_front