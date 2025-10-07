from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    extracted_evens: List[T] = []
    extracted_odds: List[T] = []
    position = 0
    while position < len(list_of_elements):
        if position % 2 == 0:
            extracted_evens.append(list_of_elements[position])
        else:
            extracted_odds.append(list_of_elements[position])
        position += 1
    extracted_evens.sort()
    merged_result: List[T] = []
    idx = 0
    limit = min(len(extracted_evens), len(extracted_odds))
    while idx < limit:
        merged_result.append(extracted_evens[idx])
        merged_result.append(extracted_odds[idx])
        idx += 1
    if len(extracted_evens) > len(extracted_odds):
        merged_result.append(extracted_evens[-1])
    return merged_result