from typing import List, TypeVar

T = TypeVar('T')


def sort_even(list_of_elements: List[T]) -> List[T]:
    idx_a: int = 0
    idx_b: int = 1  # unused variable based on pseudocode, retained for exact structure
    coll_x: List[T] = []
    coll_y: List[T] = []

    while idx_a < len(list_of_elements):
        coll_x.append(list_of_elements[idx_a])
        idx_a += 2

    idx_c: int = 1
    while idx_c < len(list_of_elements):
        coll_y.append(list_of_elements[idx_c])
        idx_c += 2

    coll_x.sort()

    merged_result: List[T] = []
    iter_z: int = 0
    limit: int = min(len(coll_x), len(coll_y))
    while iter_z < limit:
        temp_pair = (coll_x[iter_z], coll_y[iter_z])
        temp_i: int = 0
        while temp_i < 2:
            merged_result.append(temp_pair[temp_i])
            temp_i += 1
        iter_z += 1

    if len(coll_x) > len(coll_y):
        merged_result.append(coll_x[-1])

    return merged_result