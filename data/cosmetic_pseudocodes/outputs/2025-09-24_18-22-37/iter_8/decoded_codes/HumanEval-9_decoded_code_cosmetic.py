from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    current_peak: Optional[int] = None
    output_sequence: List[int] = []
    iterator_index: int = 0

    while iterator_index < len(list_of_numbers):
        current_value: int = list_of_numbers[iterator_index]

        if current_peak is None:
            current_peak = current_value
        else:
            temp_max_candidate: int = current_peak
            if temp_max_candidate < current_value:
                current_peak = current_value

        output_sequence.append(current_peak)
        iterator_index += 1

    return output_sequence