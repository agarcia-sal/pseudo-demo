class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def calculateFrequencies(text: str) -> dict:
            counts = {}
            pos = 0
            while pos < len(text):
                ch = text[pos]
                counts[ch] = counts.get(ch, 0) + 1
                pos += 1
            return counts

        def sortAscending(arr: list) -> list:
            if len(arr) <= 1:
                return arr
            middleIndex = len(arr) // 2
            leftPart = sortAscending(arr[:middleIndex])
            rightPart = sortAscending(arr[middleIndex:])
            resultList = []
            iLeft = iRight = 0
            while iLeft < len(leftPart) or iRight < len(rightPart):
                if iRight >= len(rightPart) or (iLeft < len(leftPart) and leftPart[iLeft] <= rightPart[iRight]):
                    resultList.append(leftPart[iLeft])
                    iLeft += 1
                else:
                    resultList.append(rightPart[iRight])
                    iRight += 1
            return resultList

        def equalsInfinity(val: float) -> bool:
            return val >= 1.0e+300

        freqMap = calculateFrequencies(word)
        valuesList = [freqMap[key] for key in freqMap]
        sortedFreqs = sortAscending(valuesList)

        bestScore = 1.0e+300
        idx = 0

        def sumFromIndex(start: int, endExclusive: int) -> int:
            total = 0
            p = start
            while p < endExclusive:
                total += sortedFreqs[p]
                p += 1
            return total

        while idx < len(sortedFreqs):
            maxFreqAllowed = sortedFreqs[idx] + k
            sumDeletion = 0

            posDel = idx + 1
            while posDel < len(sortedFreqs):
                if sortedFreqs[posDel] > maxFreqAllowed:
                    sumDeletion += (sortedFreqs[posDel] - maxFreqAllowed)
                posDel += 1

            sumDeletion += sumFromIndex(0, idx)
            if sumDeletion < bestScore:
                bestScore = sumDeletion
            idx += 1

        return int(bestScore)