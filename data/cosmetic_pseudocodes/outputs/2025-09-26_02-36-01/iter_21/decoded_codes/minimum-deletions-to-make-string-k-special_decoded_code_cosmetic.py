class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        alphaFrequencyMap = {}
        for currChar in word:
            alphaFrequencyMap[currChar] = alphaFrequencyMap.get(currChar, 0) + 1

        tempList = list(alphaFrequencyMap.values())

        def quickSort(arr, left, right):
            if left >= right:
                return
            pivotIdx = left
            wall = left
            for iter in range(left + 1, right + 1):
                if arr[iter] < arr[pivotIdx]:
                    wall += 1
                    arr[wall], arr[iter] = arr[iter], arr[wall]
            arr[wall], arr[pivotIdx] = arr[pivotIdx], arr[wall]
            quickSort(arr, left, wall - 1)
            quickSort(arr, wall + 1, right)

        quickSort(tempList, 0, len(tempList) - 1)
        sortedFreqVals = tempList

        globalMinDeletions = float('inf')

        def processIndex(idx):
            nonlocal globalMinDeletions
            allowedMaxFreq = sortedFreqVals[idx] + k
            calcDeletions = 0

            forwardIndex = idx + 1
            while forwardIndex < len(sortedFreqVals):
                currFreq = sortedFreqVals[forwardIndex]
                if currFreq > allowedMaxFreq:
                    calcDeletions += currFreq - allowedMaxFreq
                forwardIndex += 1

            backIndex = 0
            while backIndex < idx:
                calcDeletions += sortedFreqVals[backIndex]
                backIndex += 1

            if calcDeletions < globalMinDeletions:
                globalMinDeletions = calcDeletions

        outerIndex = 0
        while outerIndex < len(sortedFreqVals):
            processIndex(outerIndex)
            outerIndex += 1

        return globalMinDeletions