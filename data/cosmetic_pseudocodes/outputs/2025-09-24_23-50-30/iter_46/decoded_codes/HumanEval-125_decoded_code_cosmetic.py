from typing import List, Union


def split_words(str: str) -> Union[List[str], int]:

    def helper_replace_commas(s: str, i: int, acc: str) -> str:
        if i >= len(s):
            return acc
        if s[i] == ',':
            return helper_replace_commas(s, i + 1, acc + ' ')
        return helper_replace_commas(s, i + 1, acc + s[i])

    def helper_split_whitespace(s: str, i: int, current: str, acc: List[str]) -> List[str]:
        if i > len(s):
            return acc if current == '' else acc + [current]
        if i == len(s) or s[i] == ' ':
            if current == '':
                return helper_split_whitespace(s, i + 1, '', acc)
            return helper_split_whitespace(s, i + 1, '', acc + [current])
        return helper_split_whitespace(s, i + 1, current + s[i], acc)

    def helper_count_chars(s: str, i: int, c: int) -> int:
        if i >= len(s):
            return c
        ch = s[i]
        if 'a' <= ch <= 'z' and (ord(ch) % 2) == 0:
            return helper_count_chars(s, i + 1, c + 1)
        return helper_count_chars(s, i + 1, c)

    def contains_char(s: str, ch: str, idx: int) -> bool:
        if idx >= len(s):
            return False
        if s[idx] == ch:
            return True
        return contains_char(s, ch, idx + 1)

    if contains_char(str, ' ', 0):
        return helper_split_whitespace(str, 0, '', [])
    if contains_char(str, ',', 0):
        temp_str = helper_replace_commas(str, 0, '')
        return helper_split_whitespace(temp_str, 0, '', [])
    return helper_count_chars(str, 0, 0)