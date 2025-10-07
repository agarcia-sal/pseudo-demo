from typing import List


def is_nested(input_string: str) -> bool:
    list_of_opening_bracket_indices: List[int] = []
    list_of_closing_bracket_indices: List[int] = []
    for index in range(len(input_string)):
        if input_string[index] == '[':
            list_of_opening_bracket_indices.append(index)
        else:
            list_of_closing_bracket_indices.append(index)
    list_of_closing_bracket_indices.reverse()

    matched_pair_count: int = 0
    closing_index_pointer: int = 0
    total_closing_brackets: int = len(list_of_closing_bracket_indices)

    for opening_index in list_of_opening_bracket_indices:
        if (
            closing_index_pointer < total_closing_brackets
            and opening_index < list_of_closing_bracket_indices[closing_index_pointer]
        ):
            matched_pair_count += 1
            closing_index_pointer += 1

    return matched_pair_count >= 2