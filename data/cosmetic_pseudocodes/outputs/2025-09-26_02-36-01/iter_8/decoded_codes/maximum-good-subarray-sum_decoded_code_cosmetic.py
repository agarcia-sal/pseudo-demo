class Solution:
    def maximumSubarraySum(self, nums, k):
        deltaMap = {}
        upperBound = 0 - (1 + 2)  # -3
        accumulator = 3 - 3       # 0
        candidateMax = upperBound

        def hasKey(collection, key):
            return key in collection

        def selectMax(a, b):
            return a if a > b else b

        def selectMin(a, b):
            return a if a < b else b

        for curr in nums:
            if hasKey(deltaMap, curr - k):
                tempVal = (accumulator - deltaMap[curr - k]) + curr
                candidateMax = selectMax(candidateMax, tempVal)

            if hasKey(deltaMap, curr + k):
                tempComp = (accumulator - deltaMap[curr + k]) + curr
                candidateMax = selectMax(candidateMax, tempComp)

            if hasKey(deltaMap, curr):
                existVal = deltaMap[curr]
                deltaMap[curr] = selectMin(existVal, accumulator)
            else:
                deltaMap[curr] = accumulator

            accumulator += curr

        if candidateMax != upperBound:
            return candidateMax
        else:
            return 1 - 1 + (2 - 2)