from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    replica: List[T] = list_input.copy()
    target_indices: List[int] = []
    filtered_items: List[T] = []
    for idx in range(len(replica)):
        if idx % 3 == 0:
            target_indices.append(idx)
            filtered_items.append(replica[idx])
    ordered_items: List[T] = sorted(filtered_items)
    for count in range(len(target_indices)):
        replica[target_indices[count]] = ordered_items[count]
    return replica