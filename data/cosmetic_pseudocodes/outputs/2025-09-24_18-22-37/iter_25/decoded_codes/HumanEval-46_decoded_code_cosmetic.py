from typing import List


def fib4(integer_n: int) -> int:
    alphaList: List[int] = [0, 0, 2, 0]

    maxIter: int = integer_n
    elementCount: int = len(alphaList)

    if maxIter < 4:
        return alphaList[maxIter]

    indexI: int = 4
    while indexI <= maxIter:
        d: int = alphaList[elementCount - 1]
        c: int = alphaList[elementCount - 2]
        b: int = alphaList[elementCount - 3]
        a: int = alphaList[elementCount - 4]

        tempVal: int = a + b + c + d

        alphaList.append(tempVal)
        alphaList.pop(0)  # removeAt(0)

        elementCount = len(alphaList)
        indexI += 1

    return alphaList[elementCount - 1]