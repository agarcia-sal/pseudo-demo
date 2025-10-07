from typing import List

def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    accumulated_list: List[int] = []
    toggle_indicator: bool = False
    while array_of_numbers:
        toggle_indicator = not toggle_indicator
        if not toggle_indicator:
            # Find minimum value
            candidate_value = array_of_numbers[0]
            for num in array_of_numbers[1:]:
                if num < candidate_value:
                    candidate_value = num
        else:
            # Find maximum value
            candidate_value = array_of_numbers[0]
            for num in array_of_numbers[1:]:
                if not (num <= candidate_value):  # equivalent to num > candidate_value
                    candidate_value = num
        accumulated_list.append(candidate_value)
        array_of_numbers.remove(candidate_value)
    return accumulated_list