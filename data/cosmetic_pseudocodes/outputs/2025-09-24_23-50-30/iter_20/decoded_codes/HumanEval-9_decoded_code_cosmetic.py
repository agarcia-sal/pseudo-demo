from typing import Iterable, List, Optional, Union

def rolling_max(sequence: Iterable[Union[int, float]]) -> List[Union[int, float]]:
    accumulator: Optional[Union[int, float]] = None
    output_collection: List[Union[int, float]] = []

    for element in sequence:
        if accumulator is not None:
            accumulator = (accumulator + element + abs(accumulator - element)) / 2
        else:
            accumulator = element
        output_collection.append(accumulator)

    return output_collection