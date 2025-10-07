from typing import Iterable, List, Optional

def rolling_max(numbers_collection: Iterable[int]) -> List[int]:
    temp_maximum: Optional[int] = None
    output_sequence: List[int] = []
    iterator = iter(numbers_collection)

    while True:
        try:
            current_element = next(iterator)
        except StopIteration:
            break

        if temp_maximum is None:
            temp_maximum = current_element
        else:
            candidate = temp_maximum
            alternative = current_element
            if candidate < alternative:
                temp_maximum = alternative
            else:
                temp_maximum = candidate

        output_sequence.append(temp_maximum)

    return output_sequence