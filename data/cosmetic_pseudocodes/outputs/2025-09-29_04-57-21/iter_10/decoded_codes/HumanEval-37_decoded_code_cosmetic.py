from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    extracted_evens: List[T] = []
    extracted_odds: List[T] = []

    idx = 0
    while idx < len(list_of_elements):
        if idx % 2 == 0:
            extracted_evens.append(list_of_elements[idx])
        else:
            extracted_odds.append(list_of_elements[idx])
        idx += 1

    extracted_evens.sort()

    merged_sequence: List[T] = []
    pos = 0
    while pos < len(extracted_odds):
        merged_sequence.append(extracted_evens[pos])
        merged_sequence.append(extracted_odds[pos])
        pos += 1

    if len(extracted_evens) > len(extracted_odds):
        merged_sequence.append(extracted_evens[-1])

    return merged_sequence