from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_indicator: bool = False
    while list_of_integers:
        if not toggle_indicator:
            candidate_value = list_of_integers[0]
            for element in list_of_integers:
                if element < candidate_value:
                    candidate_value = element
            output_sequence.append(candidate_value)
            list_of_integers.remove(candidate_value)
        else:
            candidate_value = list_of_integers[0]
            for element in list_of_integers:
                if candidate_value < element:
                    candidate_value = element
            output_sequence.append(candidate_value)
            list_of_integers.remove(candidate_value)
        toggle_indicator = not toggle_indicator
    return output_sequence