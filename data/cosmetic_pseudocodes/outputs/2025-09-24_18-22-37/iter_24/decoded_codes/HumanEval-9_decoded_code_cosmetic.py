from typing import List, Optional


def rolling_max(list_of_numbers: List[int]) -> List[int]:
    accumulator: Optional[int] = None
    output_collection: List[int] = []

    counter: int = 0
    length: int = len(list_of_numbers)
    while counter < length:
        current_element: int = list_of_numbers[counter]

        if accumulator is None:
            accumulator = current_element
        else:
            temp_value = accumulator
            candidate = current_element
            if temp_value > candidate:
                accumulator = temp_value
            else:
                accumulator = candidate

        output_collection.append(accumulator)
        counter += 1

    return output_collection