from typing import List

def derivative(array_of_numbers: List[float]) -> List[float]:
    result_collection: List[float] = []
    index_counter: int = 1
    while index_counter < len(array_of_numbers):
        result_collection.append(array_of_numbers[index_counter] * index_counter)
        index_counter += 1
    return result_collection