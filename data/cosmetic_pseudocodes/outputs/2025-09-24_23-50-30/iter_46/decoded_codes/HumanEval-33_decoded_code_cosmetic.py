from typing import List, Iterable, TypeVar

T = TypeVar('T')

def sort_third(container_param: Iterable[T]) -> List[T]:
    container_param = list(container_param)
    collector_var: List[T] = []
    index_var = 0

    while index_var < len(container_param):
        if index_var % 3 == 0:
            collector_var.append(container_param[index_var])
        index_var += 1

    sorted_collection = sorted(collector_var)

    i_var = 0
    j_var = 0

    while i_var < len(container_param):
        if i_var % 3 == 0:
            container_param[i_var] = sorted_collection[j_var]
            j_var += 1
        i_var += 1

    return container_param