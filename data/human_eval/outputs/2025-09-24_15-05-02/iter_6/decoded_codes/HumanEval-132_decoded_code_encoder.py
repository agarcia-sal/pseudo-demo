from typing import List

def is_nested(string: str) -> bool:
    opening_bracket_indices: List[int] = []
    closing_bracket_indices: List[int] = []

    for index, char in enumerate(string):
        if char == '[':
            opening_bracket_indices.append(index)
        else:
            closing_bracket_indices.append(index)

    closing_bracket_indices.reverse()

    matched_count = 0
    i = 0
    closing_length = len(closing_bracket_indices)

    for opening_index in opening_bracket_indices:
        if i < closing_length and opening_index < closing_bracket_indices[i]:
            matched_count += 1
            i += 1

    return matched_count >= 2