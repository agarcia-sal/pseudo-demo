from typing import List, TypeVar

T = TypeVar('T')

def sort_third(input_list: List[T]) -> List[T]:
    l = list(input_list)
    indices = [i for i in range(len(l)) if i % 3 == 0]
    sublist = [l[i] for i in indices]
    sublist.sort()
    for idx, val in zip(indices, sublist):
        l[idx] = val
    return l