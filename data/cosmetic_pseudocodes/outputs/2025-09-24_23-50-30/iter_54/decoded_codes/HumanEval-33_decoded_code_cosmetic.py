from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    fresh_list: List[T] = [item for item in list_input]

    divisible_indices: List[int] = []
    extracted_values: List[T] = []
    position: int = 0
    while position < len(fresh_list):
        if position % 3 == 0:
            divisible_indices.append(position)
            extracted_values.append(fresh_list[position])
        position += 1

    sorted_extracted_values: List[T] = sorted(extracted_values)

    iterator: int = 0
    while iterator < len(divisible_indices):
        fresh_list[divisible_indices[iterator]] = sorted_extracted_values[iterator]
        iterator += 1

    return fresh_list