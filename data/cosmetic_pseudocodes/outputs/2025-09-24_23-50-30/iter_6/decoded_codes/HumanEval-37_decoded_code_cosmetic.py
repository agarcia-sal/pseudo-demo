from typing import List, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self: T, other: T) -> bool:
        ...

def sort_even(list_of_elements: List[T]) -> List[T]:
    idx_even: int = 0
    idx_odd: int = 1
    collection_even: List[T] = []
    # Collect elements at even indices
    while idx_even < len(list_of_elements):
        collection_even.append(list_of_elements[idx_even])
        idx_even += 2
    collection_odd: List[T] = []
    # Collect elements at odd indices
    while idx_odd < len(list_of_elements):
        collection_odd.append(list_of_elements[idx_odd])
        idx_odd += 2
    collection_even.sort()
    merged_result: List[T] = []
    pos: int = 0
    # Merge even and odd collections alternately
    while pos < len(collection_odd):
        merged_result.append(collection_even[pos])
        merged_result.append(collection_odd[pos])
        pos += 1
    # Append the last even element if it exists and collection_even is longer
    if len(collection_even) > len(collection_odd):
        merged_result.append(collection_even[-1])
    return merged_result