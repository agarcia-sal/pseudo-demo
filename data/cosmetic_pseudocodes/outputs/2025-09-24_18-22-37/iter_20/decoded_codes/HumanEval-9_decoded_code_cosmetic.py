from typing import List, Optional

def rolling_max(list_of_numbers: List[float]) -> List[float]:
    iterator_index: int = 0
    accumulator_max: Optional[float] = None
    output_sequence: List[float] = []
    length_of_sequence: int = len(list_of_numbers)

    while iterator_index < length_of_sequence:
        current_element: float = list_of_numbers[iterator_index]

        if accumulator_max is None:
            accumulator_max = current_element
        else:
            if accumulator_max < current_element:
                accumulator_max = current_element

        output_sequence.append(accumulator_max)
        iterator_index += 1

    return output_sequence