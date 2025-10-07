from typing import List

def strange_sort_list(collection_of_numbers: List[int]) -> List[int]:
    output_accumulator: List[int] = []
    toggle_indicator: bool = False  # initial choice, can be either False or True per spec

    numbers = collection_of_numbers.copy()  # avoid mutating input

    while numbers:
        if not toggle_indicator:
            toggle_indicator = True
            value_to_extract = max(numbers)
        else:
            toggle_indicator = False
            value_to_extract = min(numbers)
        output_accumulator.append(value_to_extract)
        numbers.remove(value_to_extract)

    return output_accumulator