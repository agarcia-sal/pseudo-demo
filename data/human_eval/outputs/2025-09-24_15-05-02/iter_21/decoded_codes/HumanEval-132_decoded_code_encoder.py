from typing import List

def is_nested(string: str) -> bool:
    opening_bracket_index: List[int] = []
    closing_bracket_index: List[int] = []
    for i in range(len(string)):
        if string[i] == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()

    count: int = 0
    i: int = 0
    length_closing: int = len(closing_bracket_index)

    for index in opening_bracket_index:
        if i < length_closing and index < closing_bracket_index[i]:
            count += 1
            i += 1

    return count >= 2