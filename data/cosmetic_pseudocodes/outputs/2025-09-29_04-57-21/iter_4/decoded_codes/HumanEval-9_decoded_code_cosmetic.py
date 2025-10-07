from typing import List, Optional

def rolling_max(list_of_numbers: List[float]) -> List[float]:
    current_peak: Optional[float] = None
    output_sequence: List[float] = []

    iterator: int = 0
    while iterator < len(list_of_numbers):
        current_value = list_of_numbers[iterator]
        if current_peak is None:
            current_peak = current_value
        else:
            if current_value > current_peak:
                current_peak = current_value
        output_sequence.append(current_peak)
        iterator += 1

    return output_sequence