from typing import List

def is_nested(string: str) -> bool:
    opening_bracket_index: List[int] = []
    closing_bracket_index: List[int] = []
    for index in range(len(string)):
        if string[index] == '[':
            opening_bracket_index.append(index)
        else:
            closing_bracket_index.append(index)
    closing_bracket_index.reverse()
    count: int = 0
    position: int = 0
    length_closing: int = len(closing_bracket_index)
    for index in opening_bracket_index:
        if position < length_closing and index < closing_bracket_index[position]:
            count += 1
            position += 1
    return count >= 2