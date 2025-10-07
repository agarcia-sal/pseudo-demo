from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    def process_with_space(
        s: str, acc: List[str], idx: int, length: int
    ) -> List[str]:
        if idx >= length:
            return acc
        if s[idx] == ' ':
            return process_with_space(s, acc + [""], idx + 1, length)
        tail = acc[-1]
        new_tail = tail + s[idx]
        return process_with_space(s, acc[:-1] + [new_tail], idx + 1, length)

    def contains_char(s: str, ch: str, pos: int, length: int) -> bool:
        if pos >= length:
            return False
        if s[pos] == ch:
            return True
        return contains_char(s, ch, pos + 1, length)

    def replace_comma_with_space(
        s: str, pos: int, length: int, builder: List[str]
    ) -> List[str]:
        if pos >= length:
            return builder
        next_char = ' ' if s[pos] == ',' else s[pos]
        return replace_comma_with_space(s, pos + 1, length, builder + [next_char])

    def count_lowercase_even_ascii(
        s: str, idx: int, length: int, cnt: int
    ) -> int:
        if idx >= length:
            return cnt
        c = s[idx]
        is_lower = 'a' <= c <= 'z'
        ascii_val = ord(c)
        even_check = (ascii_val % 2) == 0
        return (
            count_lowercase_even_ascii(s, idx + 1, length, cnt + 1)
            if is_lower and even_check
            else count_lowercase_even_ascii(s, idx + 1, length, cnt)
        )

    n = len(input_string)
    if contains_char(input_string, ' ', 0, n):
        return process_with_space(input_string, [""], 0, n)
    if contains_char(input_string, ',', 0, n):
        replaced_list = replace_comma_with_space(input_string, 0, n, [])
        replaced_str = "".join(replaced_list)
        return process_with_space(replaced_str, [""], 0, len(replaced_str))
    return count_lowercase_even_ascii(input_string, 0, n, 0)