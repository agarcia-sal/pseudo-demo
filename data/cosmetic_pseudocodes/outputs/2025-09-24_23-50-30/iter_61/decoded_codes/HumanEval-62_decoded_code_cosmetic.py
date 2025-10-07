from typing import List

def derivative(array_of_terms: List[int]) -> List[int]:
    if len(array_of_terms) <= 1:
        return []
    return build_result(array_of_terms, 1, [])

def build_result(source_array: List[int], position: int, accumulator: List[int]) -> List[int]:
    if position < len(source_array):
        temporary_value = source_array[position] * position
        updated_accumulator = accumulator + [temporary_value]
        return build_result(source_array, position + 1, updated_accumulator)
    return accumulator