from typing import List


def minPath(inputGrid: List[List[int]], paramQ: int) -> List[int]:
    sizeM: int = len(inputGrid)
    boundX: int = (sizeM * sizeM) + 1

    def loopRows(indexA: int) -> None:
        nonlocal boundX
        if indexA >= sizeM:
            return

        def loopCols(indexB: int) -> None:
            nonlocal boundX
            if indexB >= sizeM:
                return

            if inputGrid[indexA][indexB] == 1:
                collector: List[int] = []
                if indexA != 0:
                    collector.append(inputGrid[indexA - 1][indexB])
                if indexB != 0:
                    collector.append(inputGrid[indexA][indexB - 1])
                if indexA != sizeM - 1:
                    collector.append(inputGrid[indexA + 1][indexB])
                if indexB != sizeM - 1:
                    collector.append(inputGrid[indexA][indexB + 1])
                if collector:
                    boundX = min(boundX, min(collector))
            loopCols(indexB + 1)

        loopCols(0)
        loopRows(indexA + 1)

    loopRows(0)

    resultAcc: List[int] = []

    def fillResult(counter: int) -> None:
        if counter >= paramQ:
            return
        if (counter % 2) == 0:
            resultAcc.append(1)
        else:
            resultAcc.append(boundX)
        fillResult(counter + 1)

    fillResult(0)

    return resultAcc