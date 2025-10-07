from typing import List

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    current_peak: int
    output_sequence: List[int] = []
    index: int = 0

    while index < len(list_of_numbers):
        if index == 0:
            current_peak = list_of_numbers[0]
        else:
            if list_of_numbers[index] > current_peak:
                current_peak = list_of_numbers[index]
        output_sequence.append(current_peak)
        index += 1

    return output_sequence