from typing import List


def fruit_distribution(detail_string: str, fruit_total: int) -> int:
    numbers_collection: List[int] = []
    parts_list: List[str] = detail_string.split(" ")
    index_counter: int = 0
    while index_counter < len(parts_list):
        current_piece: str = parts_list[index_counter]
        if current_piece.isdigit():
            converted_number: int = int(current_piece)
            numbers_collection.append(converted_number)
        index_counter += 1
    aggregated_sum: int = 0
    for value_index in range(len(numbers_collection)):
        aggregated_sum += numbers_collection[value_index]
    result_difference: int = fruit_total - aggregated_sum
    return result_difference