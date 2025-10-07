from typing import List, TypeVar

T = TypeVar('T')

def strange_sort_list(xr: List[T]) -> List[T]:
    fq: List[T] = []
    kb: bool = True
    xr = xr.copy()  # Avoid mutating original list

    while xr:
        rv: T = min(xr) if kb else max(xr)
        fq.append(rv)
        rp = xr.index(rv)
        del xr[rp]
        kb = not kb

    return fq