from typing import List, Iterable, TypeVar, Union

T = TypeVar('T')

def sort_third(l: Union[Iterable[T], List[T]]) -> List[T]:
    l = list(l)
    indices = [i for i in range(len(l)) if i % 3 == 0]
    extracted = [l[i] for i in indices]
    extracted.sort()
    for idx, val in zip(indices, extracted):
        l[idx] = val
    return l