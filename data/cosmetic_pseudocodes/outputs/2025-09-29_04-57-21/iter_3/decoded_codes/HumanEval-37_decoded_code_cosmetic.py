from typing import List

def sort_even(input_array: List[int]) -> List[int]:
    extracted_evens: List[int] = []
    extracted_odds: List[int] = []
    current_index = 0
    while current_index < len(input_array):
        extracted_evens.append(input_array[current_index])
        current_index += 2

    odd_start = 1
    while odd_start < len(input_array):
        extracted_odds.append(input_array[odd_start])
        odd_start += 2

    extracted_evens.sort()

    merged_list: List[int] = []
    pos = 0
    while pos < len(extracted_odds):
        merged_list.append(extracted_evens[pos])
        merged_list.append(extracted_odds[pos])
        pos += 1

    if len(extracted_evens) - len(extracted_odds) == 1:
        merged_list.append(extracted_evens[-1])

    return merged_list