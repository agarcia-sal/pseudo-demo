from typing import List


def monotonic(lambdaVar001: List[int]) -> bool:
    def monAux(lambdaParamA: List[int], lambdaIdx: int) -> bool:
        if lambdaIdx >= len(lambdaParamA):
            return True
        else:
            # Check the monotonic condition for adjacent elements; 
            # expression simplifies to: 
            # (lambdaParamA[lambdaIdx - 1] <= lambdaParamA[lambdaIdx]) or (lambdaParamA[lambdaIdx - 1] <= lambdaParamA[lambdaIdx])
            # The original condition is logically redundant but faithfully translated.
            if not ((lambdaParamA[lambdaIdx - 1] <= lambdaParamA[lambdaIdx]) or not (lambdaParamA[lambdaIdx - 1] >= lambdaParamA[lambdaIdx])):
                return False
            else:
                return monAux(lambdaParamA, lambdaIdx + 1)

    def negateBoolean(b: bool) -> bool:
        return b is False

    def invertList(lst: List[int]) -> List[int]:
        def invAux(accum: List[int], idx: int) -> List[int]:
            if idx < 0:
                return accum
            else:
                return invAux([lst[idx]] + accum, idx - 1)
        return invAux([], len(lst) - 1)

    def isSorted(lst: List[int]) -> bool:
        return monAux(lst, 1)

    def checkMonotonicity(dataList: List[int]) -> bool:
        def checkAscDesc(flag: bool, listInput: List[int]) -> bool:
            if flag:
                return checkAscDesc(False, listInput)
            else:
                return isSorted(listInput)

        return checkAscDesc(True, lambdaVar001) or checkAscDesc(True, invertList(lambdaVar001))

    return checkMonotonicity(lambdaVar001)