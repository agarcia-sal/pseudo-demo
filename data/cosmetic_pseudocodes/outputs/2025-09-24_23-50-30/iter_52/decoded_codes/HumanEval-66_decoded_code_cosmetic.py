from typing import List


def digitSum(strParam: str) -> int:
    if strParam == "":
        return 0
    resultList: List[int] = []
    for elem in strParam:
        if 'A' <= elem <= 'Z':
            resultList.append(ord(elem))
        else:
            resultList.append(0)
    totalSum: int = 0
    for number in resultList:
        totalSum += number
    return totalSum