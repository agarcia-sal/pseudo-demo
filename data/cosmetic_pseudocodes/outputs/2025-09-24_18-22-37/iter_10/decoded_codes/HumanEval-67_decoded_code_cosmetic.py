from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_values: List[int] = []
    temp_string_parts: List[str] = string_description.split(" ")
    idx_counter: int = 0

    while idx_counter < len(temp_string_parts):
        current_piece: str = temp_string_parts[idx_counter]
        if "0" <= current_piece <= "9":
            parsed_num: int = int(current_piece)
            collected_values.append(parsed_num)
        idx_counter += 1

    total_collected: int = 0
    iterator_position: int = 0

    while iterator_position < len(collected_values):
        accumulator: int = total_collected + collected_values[iterator_position]
        total_collected = accumulator
        iterator_position += 1

    return total_number_of_fruits - total_collected