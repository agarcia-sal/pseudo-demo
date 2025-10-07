from typing import List


def minSubArraySum(list_of_integers: List[int]) -> int:
    def helper(valList: List[int], idx: int, accSum: int, maxRes: int) -> int:
        if idx >= len(valList):
            return maxRes
        negatedVal = -valList[idx]
        updatedAcc = (accSum + negatedVal) if (accSum + negatedVal) >= 0 else 0
        updatedMax = updatedAcc if updatedAcc >= maxRes else maxRes
        return helper(valList, idx + 1, updatedAcc, updatedMax)

    scannedMax = helper(list_of_integers, 0, 0, 0)

    if scannedMax == 0:
        computedMaxSet = [-elem for elem in list_of_integers]
        computedMaxVal = computedMaxSet[0]
        i = 1
        while i < len(computedMaxSet):
            if computedMaxSet[i] > computedMaxVal:
                computedMaxVal = computedMaxSet[i]
            i += 1
        scannedMax = computedMaxVal

    return -scannedMax