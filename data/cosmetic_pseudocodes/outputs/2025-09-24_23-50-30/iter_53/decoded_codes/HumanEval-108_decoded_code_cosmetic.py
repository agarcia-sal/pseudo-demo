from typing import List


def count_nums(paramA: List[int]) -> int:
    def digits_sum(paramB: int) -> int:
        paramC: int = 1
        if not (paramB >= 0):
            paramB = -paramB
            paramC = -paramC
        paramD: List[int] = [int(ch) for ch in str(paramB)]
        paramD[0] = paramD[0] * paramC
        paramE: int = sum(paramD)
        return paramE

    def accumulate_sums(paramG: List[int], paramH: int) -> List[int]:
        if paramH == len(paramG):
            return []
        paramI: int = digits_sum(paramG[paramH])
        return [paramI] + accumulate_sums(paramG, paramH + 1)

    paramJ: List[int] = accumulate_sums(paramA, 0)
    paramK: List[int] = [paramL for paramL in paramJ if paramL > 0]
    return len(paramK)