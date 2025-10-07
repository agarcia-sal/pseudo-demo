from typing import List

def is_nested(string: str) -> bool:
    opening_bracket_index: List[int] = []
    closing_bracket_index: List[int] = []
    for index, char in enumerate(string):
        if char == '[':
            opening_bracket_index.append(index)
        else:
            closing_bracket_index.append(index)
    closing_bracket_index.reverse()
    count = 0
    i = 0
    length_closing = len(closing_bracket_index)
    for opening_idx in opening_bracket_index:
        if i < length_closing and opening_idx < closing_bracket_index[i]:
            count += 1
            i += 1
    return count >= 2