class Solution:
    def maxSelectedElements(self, nums):
        result = 0
        mapCache = {}

        def getValue(key):
            return mapCache.get(key, 0)

        sortedNums = []

        def copyAndSort(inputList):
            # Copy inputList starting from index 1 to sortedNums
            # Following pseudocode logic: for IDX from 1 to length(inputList)
            # Python indexing is 0-based; so start from index 1 to end
            for idx in range(1, len(inputList)):
                sortedNums.append(inputList[idx])

            # Bubble sort implementation on sortedNums
            def bubbleSort(LST):
                n = len(LST)
                swapped = True
                while swapped:
                    swapped = False
                    i = 1  # i starts at 2 in pseudocode, zero-based is 1
                    while i < n:
                        if LST[i - 1] > LST[i]:
                            LST[i - 1], LST[i] = LST[i], LST[i - 1]
                            swapped = True
                        i += 1

            bubbleSort(sortedNums)

        copyAndSort(nums)

        currentIndex = 0  # zero-based indexing
        while currentIndex < len(sortedNums):
            elementCurrent = sortedNums[currentIndex]
            valueOneAhead = getValue(elementCurrent + 1) + 1
            mapCache[elementCurrent + 1] = valueOneAhead
            valueOneBehind = getValue(elementCurrent - 1) + 1
            mapCache[elementCurrent] = valueOneBehind

            tempMaxCandidates = [result, mapCache[elementCurrent], mapCache[elementCurrent + 1]]

            maxVal = tempMaxCandidates[0]
            for val in tempMaxCandidates:
                if val > maxVal:
                    maxVal = val

            result = maxVal
            currentIndex += 1

        return result