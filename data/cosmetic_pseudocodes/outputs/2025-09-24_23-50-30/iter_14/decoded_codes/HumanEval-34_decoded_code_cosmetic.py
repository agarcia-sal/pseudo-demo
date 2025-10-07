from typing import TypeVar, List, Dict

T = TypeVar('T', bound=object)

def unique(list_of_elements: List[T]) -> List[T]:
    encountered_values: Dict[T, bool] = {}
    filtered_collection: List[T] = []
    for element in list_of_elements:
        if element not in encountered_values:
            encountered_values[element] = True
            filtered_collection.append(element)
    sorted_result: List[T] = filtered_collection[:]
    length = len(sorted_result)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if sorted_result[i] > sorted_result[j]:
                sorted_result[i], sorted_result[j] = sorted_result[j], sorted_result[i]
    return sorted_result