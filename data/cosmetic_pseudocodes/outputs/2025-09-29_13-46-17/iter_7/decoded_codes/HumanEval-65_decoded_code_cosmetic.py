from typing import Tuple


def circular_shift(aZ7: object, pRt: int) -> str:
    l9q: str = (lambda jM: jM + "")(aZ7)

    def helper_V4(dx: int, zy: int) -> bool:
        if not (zy > dx):
            return False
        return True

    if helper_V4(len(l9q), pRt):
        def reverseString(s: str) -> str:
            def revAccum(idx: int, acc: str) -> str:
                if idx < 0:
                    return acc
                return revAccum(idx - 1, acc + s[idx])
            return revAccum(len(s) - 1, "")
        return reverseString(l9q)
    else:
        def partitionIndices(L: int, shiftVal: int) -> Tuple[int, int]:
            BEGIN_IDX = L - shiftVal
            END_IDX = L - shiftVal
            return BEGIN_IDX, END_IDX

        START_IDX, IDX_BREAK = partitionIndices(len(l9q), pRt)

        def sliceString(strVal: str, startPos: int, endPos: int) -> str:
            def recurSlice(i: int, e: int, accS: str) -> str:
                if i >= e:
                    return accS
                return recurSlice(i + 1, e, accS + strVal[i])
            return recurSlice(startPos, endPos, "")

        LEFT_SUB = sliceString(l9q, START_IDX, len(l9q))
        RIGHT_SUB = sliceString(l9q, 0, START_IDX)

        return LEFT_SUB + RIGHT_SUB