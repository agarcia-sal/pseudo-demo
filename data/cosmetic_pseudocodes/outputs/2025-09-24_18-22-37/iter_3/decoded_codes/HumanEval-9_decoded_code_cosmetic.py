from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    accumulator: Optional[int] = None
    output_sequence: List[int] = []

    def process(index: int) -> None:
        nonlocal accumulator
        if index >= len(list_of_numbers):
            return
        current_element = list_of_numbers[index]
        if accumulator is None:
            accumulator = current_element
        else:
            if accumulator < current_element:
                accumulator = current_element
        output_sequence.append(accumulator)
        process(index + 1)

    process(0)
    return output_sequence