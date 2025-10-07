from typing import List

def is_nested(input_string: str) -> bool:
    opening_bracket_index: List[int] = []
    closing_bracket_index: List[int] = []

    for i in range(len(input_string)):
        ch: str = input_string[i]
        if ch == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)

    closing_bracket_index.reverse()

    count: int = 0
    i: int = 0
    l: int = len(closing_bracket_index)

    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            count += 1
            i += 1

    return count >= 2