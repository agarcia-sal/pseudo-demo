from typing import List


def is_nested(input_string: str) -> bool:
    list_of_opening_indices: List[int] = []
    list_of_closing_indices: List[int] = []

    for index, char in enumerate(input_string):
        if char == '[':
            list_of_opening_indices.append(index)
        else:
            list_of_closing_indices.append(index)

    list_of_closing_indices.reverse()

    matched_count = 0
    closing_index_pointer = 0
    total_closing = len(list_of_closing_indices)

    for opening_index in list_of_opening_indices:
        if closing_index_pointer < total_closing and opening_index < list_of_closing_indices[closing_index_pointer]:
            matched_count += 1
            closing_index_pointer += 1

    return matched_count >= 2