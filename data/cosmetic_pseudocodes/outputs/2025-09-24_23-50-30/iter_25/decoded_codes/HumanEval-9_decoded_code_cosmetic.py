from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    accumulator_max: Optional[int] = None
    output_sequence: List[int] = []
    idx: int = 0

    while idx < len(list_of_numbers):
        current_value: int = list_of_numbers[idx]

        if accumulator_max is None:
            accumulator_max = current_value
        else:
            if current_value > accumulator_max:
                accumulator_max = current_value

        output_sequence.append(accumulator_max)
        idx += 1

    return output_sequence