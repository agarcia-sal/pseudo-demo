from typing import Dict, List


def histogram(λΞφΩ: str) -> Dict[str, int]:
    frequencyDict: Dict[str, int] = {}
    lettersList: List[str] = []
    maxCounter: int = 0

    def computeList(χπ: str) -> List[str]:
        if χπ == "":
            return []
        # Split the first character and remainder
        head, tail = χπ[0], χπ[1:]
        return [head] + computeList(tail)

    lettersList = computeList(λΞφΩ)

    def countOccurrences(αβζ: List[str], ρσψ: str) -> int:
        def recurCount(ξ: List[str], acc: int) -> int:
            if not ξ:
                return acc
            return recurCount(ξ[1:], acc + 1 if ξ[0] == ρσψ else acc)

        return recurCount(αβζ, 0)

    def findMax(δList: List[str], curMax: int) -> int:
        if not δList:
            return curMax
        current = δList[0]
        rest = δList[1:]
        currentCount = countOccurrences(lettersList, current)
        newMax = currentCount if current != "" and currentCount > curMax else curMax
        return findMax(rest, newMax)

    maxCounter = findMax(lettersList, 0)

    def buildFreqDict(
        σList: List[str], maxCnt: int, fDict: Dict[str, int]
    ) -> Dict[str, int]:
        if not σList:
            return fDict
        current = σList[0]
        rest = σList[1:]
        currentCount = countOccurrences(lettersList, current)
        if currentCount == maxCnt:
            # Update the dict with the current letter count
            fDict[current] = maxCnt
            return buildFreqDict(rest, maxCnt, fDict)
        else:
            return buildFreqDict(rest, maxCnt, fDict)

    if maxCounter > 0:
        frequencyDict = buildFreqDict(lettersList, maxCounter, frequencyDict)

    return frequencyDict