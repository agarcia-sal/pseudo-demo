from typing import Iterable, Optional, Union

def next_smallest(sequence_of_numbers: Iterable[Union[int, float]]) -> Optional[Union[int, float]]:
    temp_collection: list[Union[int, float]] = []
    for num in sequence_of_numbers:
        if num not in temp_collection:
            temp_collection.append(num)
    index_a = 0
    while index_a < len(temp_collection) - 1:
        index_b = index_a + 1
        while index_b < len(temp_collection):
            if temp_collection[index_a] > temp_collection[index_b]:
                temp_collection[index_a], temp_collection[index_b] = temp_collection[index_b], temp_collection[index_a]
            index_b += 1
        index_a += 1
    if len(temp_collection) <= 1:
        return None
    else:
        return temp_collection[1]