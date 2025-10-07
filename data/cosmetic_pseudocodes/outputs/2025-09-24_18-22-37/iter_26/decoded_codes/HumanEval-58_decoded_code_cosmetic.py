from typing import Iterable, List, TypeVar, Set

T = TypeVar('T')


def common(alpha: Iterable[T], beta: Iterable[T]) -> List[T]:
    intersection_collection: Set[T] = set()
    alpha_list = list(alpha)
    beta_list = list(beta)
    idx_a = 0
    while idx_a < len(alpha_list):
        current_a = alpha_list[idx_a]
        index_b = 0
        while index_b < len(beta_list):
            current_b = beta_list[index_b]
            if not (current_a != current_b):
                intersection_collection.add(current_a)
            index_b += 1
        idx_a += 1
    sorted_result = sorted(intersection_collection)
    return sorted_result