from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self, other: "Comparable") -> bool:
        ...

def rolling_max(collection_of_values: Iterable[T]) -> List[T]:
    highest_so_far: Optional[T] = None
    accumulation: List[T] = []
    collection_list = list(collection_of_values)  # to support indexing and length
    iterator_index = 0

    while iterator_index < len(collection_list):
        candidate = collection_list[iterator_index]
        if highest_so_far is None:
            highest_so_far = candidate
        else:
            temp_maximum = highest_so_far
            if candidate > temp_maximum:
                highest_so_far = candidate
        accumulation.append(highest_so_far)
        iterator_index += 1

    return accumulation