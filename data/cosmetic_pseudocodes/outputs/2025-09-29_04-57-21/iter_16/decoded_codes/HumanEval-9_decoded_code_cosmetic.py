from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    running_peak: Optional[int] = None
    output_sequence: List[int] = []

    index: int = 0
    while index < len(list_of_numbers):
        current_value = list_of_numbers[index]
        if running_peak is None:
            running_peak = current_value
        else:
            if current_value > running_peak:
                running_peak = current_value
        output_sequence.append(running_peak)
        index += 1

    return output_sequence