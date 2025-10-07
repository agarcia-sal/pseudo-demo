from typing import List

def sort_even(array_input: List[int]) -> List[int]:
    extracted_evens: List[int] = []
    extracted_odds: List[int] = []
    position_tracker: int = 0
    length: int = len(array_input)
    while position_tracker < length:
        extracted_evens.append(array_input[position_tracker])
        position_tracker += 2
    next_position: int = 1
    while next_position < length:
        extracted_odds.append(array_input[next_position])
        next_position += 2
    extracted_evens.sort()  # sort in non-decreasing order
    merged_list: List[int] = []
    iterator_even: int = 0
    length_even: int = len(extracted_evens)
    length_odd: int = len(extracted_odds)
    while iterator_even < length_odd:
        merged_list.append(extracted_evens[iterator_even])
        merged_list.append(extracted_odds[iterator_even])
        iterator_even += 1
    if not (length_even <= length_odd):
        merged_list.append(extracted_evens[length_even - 1])
    return merged_list