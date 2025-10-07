from typing import List

def derivative(array_of_values: List[float]) -> List[float]:
    result_collection: List[float] = []
    index_counter: int = 0
    for element in array_of_values:
        if index_counter > 0:
            result_collection.append(index_counter * element)
        index_counter += 1
    return result_collection