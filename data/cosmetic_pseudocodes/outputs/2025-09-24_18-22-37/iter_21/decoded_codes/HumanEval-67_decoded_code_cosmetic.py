from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_numbers: List[int] = []
    split_elements: List[str] = string_description.split(" ")
    index_counter: int = 0

    while index_counter < len(split_elements):
        current_piece: str = split_elements[index_counter]
        if not current_piece.isdigit():
            index_counter += 1
            continue
        numeric_value: int = int(current_piece)
        collected_numbers.append(numeric_value)
        index_counter += 1

    sum_of_collected: int = 0
    position: int = 0
    while True:
        if position >= len(collected_numbers):
            break
        sum_of_collected += collected_numbers[position]
        position += 1

    return total_number_of_fruits - sum_of_collected