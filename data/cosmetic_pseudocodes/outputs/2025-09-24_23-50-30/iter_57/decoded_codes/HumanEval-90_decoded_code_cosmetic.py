from typing import Iterable, Optional, Union

def next_smallest(sequence_of_numbers: Iterable[Union[int, float]]) -> Optional[Union[int, float]]:
    temp_collection: list[Union[int, float]] = []
    for element in sequence_of_numbers:
        if element not in temp_collection:
            temp_collection.append(element)
    temp_collection.sort()
    if len(temp_collection) < 2:
        return None
    else:
        return temp_collection[1]