from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    numeric_values_collection: List[int] = []
    position_index: int = 0
    length: int = len(string_description)
    while position_index < length:
        next_space_pos = string_description.find(" ", position_index)
        if next_space_pos == -1:
            token = string_description[position_index:length]
            position_index = length
        else:
            token = string_description[position_index:next_space_pos]
            position_index = next_space_pos + 1
        is_all_digits = True
        char_index = 0
        while char_index < len(token) and is_all_digits:
            is_all_digits = '0' <= token[char_index] <= '9'
            char_index += 1
        if is_all_digits and token:
            numeric_values_collection.append(int(token))
    total_sum = sum(numeric_values_collection)
    return total_number_of_fruits - total_sum