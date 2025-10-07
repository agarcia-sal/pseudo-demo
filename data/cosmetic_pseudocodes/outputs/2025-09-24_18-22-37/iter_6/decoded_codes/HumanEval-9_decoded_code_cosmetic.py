from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    accumulator: Optional[int] = None
    output_sequence: List[int] = []
    index: int = 0

    while index < len(list_of_numbers):
        current_value = list_of_numbers[index]
        if accumulator is None:
            accumulator = current_value
        else:
            if accumulator > current_value:
                pass  # accumulator remains unchanged
            else:
                accumulator = current_value
        output_sequence.append(accumulator)
        index += 1

    return output_sequence