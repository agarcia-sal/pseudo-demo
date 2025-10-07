from typing import List, Sequence, TypeVar

T = TypeVar('T')

def sort_third(collection_param: List[T]) -> List[T]:
    duplicate_container: List[T] = [collection_param[i] for i in range(len(collection_param)) if i % 3 == 0]
    ordered_container: List[T] = sorted(duplicate_container)
    position_counter: int = 0
    for idx in range(len(collection_param)):
        if idx % 3 != 0:
            continue
        collection_param[idx] = ordered_container[position_counter]
        position_counter += 1
    return collection_param