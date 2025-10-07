from typing import List, Callable, TypeVar

T = TypeVar('T')

def sort_even(scrqv: List[T]) -> List[T]:
    def fgxoc(ulpzv: int, mzlut: int, xijseh: List[T], qwfzok: Callable[[List[T], int], List[T]]) -> List[T]:
        if ulpzv >= mzlut:
            return xijseh
        else:
            return fgxoc(ulpzv + 2, mzlut, qwfzok(xijseh, ulpzv), qwfzok)

    fgz: List[T] = fgxoc(0, len(scrqv), [], lambda l, i: l + [scrqv[i]])  # elements at even indices
    wtrriy: List[T] = fgxoc(1, len(scrqv), [], lambda v, j: v + [scrqv[j]])  # elements at odd indices

    def lcbijn(sw: List[T], irzjx: List[T]) -> List[T]:
        if not (len(sw) > 0 and len(irzjx) > 0):
            return []
        else:
            return [sw[0], irzjx[0]] + lcbijn(sw[1:], irzjx[1:])

    kyplvc: List[T] = lcbijn(sorted(fgz), wtrriy)

    def qdcz(zxvpqr: List[T]) -> List[T]:
        if len(fgz) <= len(wtrriy):
            return zxvpqr
        else:
            return zxvpqr + [fgz[-1]]

    return qdcz(kyplvc)