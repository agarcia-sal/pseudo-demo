from typing import List, Optional


def prod_signs(inp_list: Optional[List[int]]) -> Optional[int]:
    if not inp_list or len(inp_list) == 0:
        return None

    zeroFound: bool = False
    negCount: int = 0
    idx: int = 0

    while idx < len(inp_list):
        if inp_list[idx] == 0:
            zeroFound = True
        else:
            if inp_list[idx] < 0:
                negCount += 1
        idx += 1

    if zeroFound:
        finalSign: int = 0
    else:
        tempPower: int = 1
        powerCounter: int = 0
        while powerCounter < negCount:
            tempPower *= -1
            powerCounter += 1
        finalSign = tempPower

    totalMagnitude: int = 0
    index2: int = 0
    while index2 < len(inp_list):
        absVal: int
        if inp_list[index2] < 0:
            absVal = -inp_list[index2]
        else:
            absVal = inp_list[index2]
        totalMagnitude += absVal
        index2 += 1

    return finalSign * totalMagnitude