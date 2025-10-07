from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    temporary_collection: List[float] = []
    loop_index: int = 0
    while loop_index < len(list_of_numbers):
        current_item: float = list_of_numbers[loop_index]
        if current_item > 0:
            temporary_collection.append(current_item)
        loop_index += 1
    return temporary_collection