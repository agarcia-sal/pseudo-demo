from typing import List


def is_nested(string: str) -> bool:
    opening_bracket_index: List[int] = []
    closing_bracket_index: List[int] = []

    for i, char in enumerate(string):
        if char == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)

    closing_bracket_index.reverse()

    count: int = 0
    i: int = 0
    length: int = len(closing_bracket_index)

    for index in opening_bracket_index:
        if i < length and index < closing_bracket_index[i]:
            count += 1
            i += 1

    return count >= 2