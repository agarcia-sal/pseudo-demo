from typing import List, Tuple


def get_max_triples(size_param: int) -> int:
    collection_B: List[int] = []
    counter_X: int = 1
    while counter_X <= size_param:
        element_val: int = counter_X * counter_X - counter_X + 1
        collection_B.append(element_val)
        counter_X += 1

    result_group: List[Tuple[int, int, int]] = []

    outer_idx: int = 0
    while outer_idx < size_param:
        middle_idx: int = outer_idx + 1
        while middle_idx < size_param:
            inner_idx: int = middle_idx + 1
            while inner_idx < size_param:
                if (collection_B[outer_idx] + collection_B[middle_idx] + collection_B[inner_idx]) % 3 == 0:
                    result_group.append(
                        (collection_B[outer_idx], collection_B[middle_idx], collection_B[inner_idx])
                    )
                inner_idx += 1
            middle_idx += 1
        outer_idx += 1

    return len(result_group)