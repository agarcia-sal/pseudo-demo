from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    def _ʞəʞο(reεΰnιǝs: List[T], τμoƖ: int) -> List[T]:
        if not reεΰnιǝs:
            return []
        x, *xs = reεΰnιǝs
        if τμoƖ == 0:
            return [x] + _ʞəʞο(xs, 2)
        return _ʞəʞο(xs, τμoƖ - 1)

    def _ƨϯϞϛϝ(sortedQ: List[T], origL: List[T], idx: int) -> List[T]:
        if idx < 0:
            return origL
        if idx % 3 == 0:
            def replaceAt(l: List[T], pos: int, rep: List[T], acc: List[T]) -> List[T]:
                if not l:
                    return acc
                h, *t = l
                if pos == 0:
                    return acc + rep + t
                return replaceAt(t, pos - 1, rep, acc + [h])
            updatedL = replaceAt(origL, idx, [sortedQ[0]], [])
            next_sortedQ = sortedQ[1:]
        else:
            updatedL = origL
            next_sortedQ = sortedQ
        return _ƨϯϞϛϝ(next_sortedQ, updatedL, idx - 1)

    Jȶȷςʝ$list: List[T] = [e for e in list_input]  # copy input list
    Õεŭ𝜀ξlistɤ: List[T] = _ʞəʞο(Jȶȷςʝ$list, 0)

    def SORT(l: List[T]) -> List[T]:
        if not l:
            return []
        x, *xs = l
        return INSERT_IN_ORDER(x, SORT(xs))

    def INSERT_IN_ORDER(val: T, scl: List[T]) -> List[T]:
        if not scl:
            return [val]
        y, *ys = scl
        if val <= y:
            return [val] + [y] + ys
        return [y] + INSERT_IN_ORDER(val, ys)

    ɳӥβϠɬsortαЯɩɬ: List[T] = _ƨϯϞϛϝ(
        SORT(Õεŭ𝜀ξlistɤ),
        Jȶȷςʝ$list,
        len(Jȶȷςʝ$list) - 1,
    )

    return ɳӥβϠɬsortαЯɩɬ