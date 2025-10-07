from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    positive_collection: List[float] = []
    index_counter: int = 0
    total_elements: int = len(list_of_numbers)

    while index_counter < total_elements:
        current_value: float = list_of_numbers[index_counter]
        if not (current_value <= 0):
            positive_collection.append(current_value)
        index_counter += 1

    return positive_collection