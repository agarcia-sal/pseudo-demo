from typing import List, Sequence, TypeVar

T = TypeVar("T")

def sort_third(list_l: Sequence[T]) -> List[T]:
    list_l = list(list_l)
    indices = [i for i in range(len(list_l)) if i % 3 == 0]
    extracted = [list_l[i] for i in indices]
    extracted.sort()
    for idx, val in zip(indices, extracted):
        list_l[idx] = val
    return list_l