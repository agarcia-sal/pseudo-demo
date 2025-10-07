class Solution:
    def maximumLength(self, nums):
        def countOccurrences(lst):
            tracker = {}

            def incrementCount(val):
                if val in tracker:
                    tracker[val] += 1
                else:
                    tracker[val] = 1

            idx = 0
            while idx < len(lst):
                incrementCount(lst[idx])
                idx += 1
            return tracker

        frequencyMap = countOccurrences(nums)
        memoLengths = {}

        def computeLength(z):
            if z not in frequencyMap or frequencyMap[z] < 2:
                if z in frequencyMap and frequencyMap[z] >= 1:
                    return 1
                else:
                    return 0
            if z in memoLengths:
                return memoLengths[z]

            def powSquare(value):
                return value * value

            squaredValue = powSquare(z)
            recursiveResult = computeLength(squaredValue)
            memoLengths[z] = recursiveResult + 2
            return memoLengths[z]

        bestLength = 1
        keysList = list(frequencyMap.keys())
        position = len(keysList) - 1

        while position >= 0:
            currentKey = keysList[position]
            if currentKey == 1:
                countVal = frequencyMap[currentKey]
                pairedCount = (countVal - 1) - ((countVal % 2) * 2)
                if bestLength < pairedCount:
                    bestLength = pairedCount
            else:
                lengthComputed = computeLength(currentKey)
                if bestLength < lengthComputed:
                    bestLength = lengthComputed
            position -= 1

        return bestLength