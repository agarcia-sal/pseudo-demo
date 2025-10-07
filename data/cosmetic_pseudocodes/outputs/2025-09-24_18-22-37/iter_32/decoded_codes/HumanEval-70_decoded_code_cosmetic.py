from typing import List

def strange_sort_list(array_numbers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_indicator: bool = True

    while array_numbers:
        if not toggle_indicator:
            chosen_element: int = max(array_numbers)
        else:
            chosen_element: int = min(array_numbers)

        output_sequence.append(chosen_element)

        for index in range(len(array_numbers)):
            if array_numbers[index] == chosen_element:
                array_numbers.pop(index)
                break

        toggle_indicator = not toggle_indicator

    return output_sequence