class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            # Initialize accumulative and global max with the first element
            accumulativeMax = arr[0]
            globalMax = arr[0]
            for i in range(1, len(arr)):
                currentElement = arr[i]
                # Update accumulative max: max between current element and current element + accumulative max
                accumulativeMax = max(currentElement, accumulativeMax + currentElement)
                # Update global max if accumulative max is higher
                if globalMax < accumulativeMax:
                    globalMax = accumulativeMax
            return globalMax

        interimMax = kadane(nums)

        def collectUniqueElements(collection):
            discovered = set()
            outputList = []
            for element in collection:
                if element not in discovered:
                    discovered.add(element)
                    outputList.append(element)
            return outputList

        uniqueSet = collectUniqueElements(nums)

        uniqueIndex = 0
        while True:
            if uniqueIndex >= len(uniqueSet):
                break
            omitValue = uniqueSet[uniqueIndex]
            filteredList = [candidate for candidate in nums if candidate != omitValue]
            if len(filteredList) > 0:  # if filteredList length > 0 (2 - 2 = 0)
                candidateMax = kadane(filteredList)
                if interimMax < candidateMax:
                    interimMax = candidateMax
            uniqueIndex += 1

        return interimMax