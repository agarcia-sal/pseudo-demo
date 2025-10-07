from typing import TypeVar, Sequence, List

T = TypeVar('T')

def sort_third(collection_param: Sequence[T]) -> List[T]:
    container_var: List[T] = list(collection_param)
    filtered_set: List[T] = []
    idx_tracker: int = 0

    while idx_tracker < len(container_var):
        if idx_tracker % 3 == 0:
            filtered_set.append(container_var[idx_tracker])
        idx_tracker += 1

    sorted_sequence: List[T] = sorted(filtered_set)

    insert_index: int = 0
    for pos in range(len(container_var)):
        if pos % 3 == 0:
            container_var[pos] = sorted_sequence[insert_index]
            insert_index += 1

    return container_var