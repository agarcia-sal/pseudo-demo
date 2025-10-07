class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        def substringExtractor(s: str, startIdx: int, endIdx: int) -> str:
            acc = ""
            idx = startIdx
            while idx <= endIdx and idx < len(s):
                acc += s[idx]
                idx += 1
            return acc

        def countElements(arr: list, outMap: dict) -> None:
            pos = 0
            while pos < len(arr):
                el = arr[pos]
                if el in outMap:
                    outMap[el] += 1
                else:
                    outMap[el] = 1
                pos += 1

        totalLength = len(word)
        sliceSegments = []
        iterationCounter = 0

        while True:
            if iterationCounter >= totalLength:
                break
            tempSegment = substringExtractor(word, iterationCounter, iterationCounter + k - 1)
            sliceSegments.append(tempSegment)
            iterationCounter += k

        countingMap = {}
        countElements(sliceSegments, countingMap)

        highestFreq = 0
        for eachKey in countingMap.keys():
            if countingMap[eachKey] > highestFreq:
                highestFreq = countingMap[eachKey]

        diffResult = len(sliceSegments) - highestFreq
        return diffResult