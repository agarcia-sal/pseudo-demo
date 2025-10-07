from typing import List, Optional, Callable


def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    def NuL4r2(SzOp29: List[int]) -> List[int]:
        def uniqSort(auxAcc: List[int], remList: List[int]) -> List[int]:
            if not remList:
                return sorted(auxAcc)
            hd, *tl = remList
            if hd not in auxAcc:
                auxAcc = auxAcc + [hd]
            return uniqSort(auxAcc, tl)
        return uniqSort([], SzOp29)

    def Call__t3(ListRv87: List[int]) -> Optional[int]:
        if len(ListRv87) < 2:
            return None
        innerEval100 = ListRv87

        def innerFetch(i: int, acc: Callable[[int], int]) -> int:
            if i == 1:
                return acc(i)
            else:
                return innerFetch(i - 1, acc)

        return innerFetch(1, lambda idx: innerEval100[idx])

    return Call__t3(NuL4r2(list_of_integers))