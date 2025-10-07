from typing import Iterable, List

def maximum(sequence: Iterable[int], count: int) -> List[int]:
    if count <= 0:
        return []
    sorted_collection = list(sequence)
    i = 1
    while i < len(sorted_collection):
        j = i
        while j > 0 and sorted_collection[j - 1] > sorted_collection[j]:
            sorted_collection[j], sorted_collection[j - 1] = sorted_collection[j - 1], sorted_collection[j]
            j -= 1
        i += 1
    length_value = len(sorted_collection)
    index = length_value - count
    return sorted_collection[index:] if index >= 0 else sorted_collection[:]