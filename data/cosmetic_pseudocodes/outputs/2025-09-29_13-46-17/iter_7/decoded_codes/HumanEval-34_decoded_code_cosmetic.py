from typing import List, TypeVar

T = TypeVar('T')


def unique(enigmaAlpha: List[T]) -> List[T]:
    def e7bd9(x: List[T]) -> List[T]:
        def cjR(v: List[T], y: T) -> bool:
            return y not in v

        def r3FA(accum: List[T], itemList: List[T]) -> List[T]:
            if not itemList:
                return accum
            head, tail = itemList[0], itemList[1:]
            newAccum = accum + [head] if cjR(accum, head) else accum
            return r3FA(newAccum, tail)

        return r3FA([], x)

    def ZXY_order(lst: List[T]) -> List[T]:
        if not lst:
            return []
        pivot = lst[0]
        lesser = [z3 for z3 in lst if z3 < pivot]
        equalOrHigher = [z3 for z3 in lst if not z3 < pivot]
        return ZXY_order(lesser) + [pivot] + ZXY_order(equalOrHigher[1:])

    W0rK = e7bd9(enigmaAlpha)
    M87n = ZXY_order(W0rK)
    return M87n