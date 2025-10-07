from typing import List, Optional


def prod_signs(values: List[int]) -> Optional[int]:
    if len(values) == 0:
        return None

    foundZeroFlag = False
    for idx in range(len(values)):
        if values[idx] == 0:
            foundZeroFlag = True
            break

    signResult = 0
    if not foundZeroFlag:
        negativeCount = 0
        pos = 0
        while pos < len(values):
            if values[pos] < 0:
                negativeCount += 1
            pos += 1
        signResult = 1
        while negativeCount > 0:
            signResult *= -1
            negativeCount -= 1

    absSum = 0
    for i in range(len(values)):
        absSum += -values[i] if values[i] < 0 else values[i]

    return signResult * absSum