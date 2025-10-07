from typing import Sequence

def add(collection_of_numbers: Sequence[int]) -> int:
    total_accumulator: int = 0
    current_index: int = 1
    collection_size: int = len(collection_of_numbers)

    while current_index <= collection_size:
        element_value: int = collection_of_numbers[current_index - 1]  # 1-based to 0-based index
        is_even_flag: bool = (element_value % 2) == 0

        if is_even_flag:
            total_accumulator += element_value

        current_index += 2

    return total_accumulator