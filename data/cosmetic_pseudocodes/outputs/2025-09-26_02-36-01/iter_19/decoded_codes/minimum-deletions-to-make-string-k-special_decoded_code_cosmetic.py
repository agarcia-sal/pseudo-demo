class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def tallyCharacters(text: str) -> dict:
            countsDict = {}
            position = 0
            while position < len(text):
                symbol = text[position]
                if symbol not in countsDict:
                    countsDict[symbol] = 1
                else:
                    countsDict[symbol] += 1
                position += 1
            return countsDict

        freqMap = tallyCharacters(word)
        freqList = [freqMap[key] for key in freqMap]

        ascSortedFreq = []
        while freqList:
            smallest = freqList[0]
            smallestIndex = 0
            checker = 1
            while checker < len(freqList):
                if freqList[checker] < smallest:
                    smallest = freqList[checker]
                    smallestIndex = checker
                checker += 1
            ascSortedFreq.append(smallest)
            freqList.pop(smallestIndex)

        bestDeleteCount = float('inf')
        idx = 0
        while idx < len(ascSortedFreq):
            allowedMax = ascSortedFreq[idx] + k
            accDelete = 0

            pos1 = idx + 1
            while pos1 < len(ascSortedFreq):
                if ascSortedFreq[pos1] > allowedMax:
                    accDelete += ascSortedFreq[pos1] - allowedMax
                pos1 += 1

            pos2 = 0
            while pos2 < idx:
                accDelete += ascSortedFreq[pos2]
                pos2 += 1

            if accDelete < bestDeleteCount:
                bestDeleteCount = accDelete

            idx += 1
        return bestDeleteCount