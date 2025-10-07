from typing import List


def count_nums(paramA: List[int]) -> int:
    def digits_sum(paramB: int) -> int:
        varX = 1
        if paramB < 0:
            paramB = -paramB
            varX = -1
        varY = [int(ch) for ch in str(paramB)]
        varY[0] *= varX
        varZ = sum(varY)
        return varZ

    varM: List[int] = []
    idxN = 0
    while idxN < len(paramA):
        valP = paramA[idxN]
        varM.append(digits_sum(valP))
        idxN += 1

    varR: List[int] = []
    idxS = 0
    while idxS < len(varM):
        if varM[idxS] > 0:
            varR.append(varM[idxS])
        idxS += 1

    return len(varR)