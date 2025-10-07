from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    kffqvdjkwvn: List[T] = list_input.copy()
    rtgcbvmsuette: List[T] = []
    i: int = 0
    while i < len(kffqvdjkwvn):
        if i % 3 == 0:
            qyxoemtzbn: T = kffqvdjkwvn[i]
            rtgcbvmsuette.append(qyxoemtzbn)
        i += 1

    ikfgzmmanuq: List[T] = rtgcbvmsuette
    ikfgzmmanuq.sort()

    j: int = 0
    n: int = len(kffqvdjkwvn)
    m: int = len(ikfgzmmanuq)
    fgswlzsmwn: int = 0
    while fgswlzsmwn < n:
        mod_val = fgswlzsmwn % 3
        if mod_val == 0:
            if j < m:
                kffqvdjkwvn[fgswlzsmwn] = ikfgzmmanuq[j]
                j += 1
        fgswlzsmwn += 1

    return kffqvdjkwvn