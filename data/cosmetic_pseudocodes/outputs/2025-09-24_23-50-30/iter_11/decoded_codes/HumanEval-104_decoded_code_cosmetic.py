from typing import List


def unique_digits(collection_of_numbers: List[int]) -> List[int]:
    filtered_numbers: List[int] = []
    index_counter: int = 0
    while index_counter < len(collection_of_numbers):
        current_value: int = collection_of_numbers[index_counter]
        # Check if no digit in current_value is even
        if not any((int(digit) % 2 == 0) for digit in str(current_value)):
            filtered_numbers.append(current_value)
        index_counter += 1
    return sorted(filtered_numbers)