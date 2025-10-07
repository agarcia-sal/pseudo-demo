from collections import defaultdict

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        def replicateDefaultDict():
            return defaultdict(int)

        A = replicateDefaultDict()
        B = replicateDefaultDict()

        for val in nums:
            A[val] += 1
            B[val] += 0

            key1 = val - k
            B[key1] += 1

            key2 = val + k + 1
            B[key2] -= 1

        maximumFrequency = 0
        runningSum = 0

        sortedKeys = sorted(B.keys())

        pos = 0
        while pos < len(sortedKeys):
            currentKey = sortedKeys[pos]
            runningSum += B[currentKey]

            candidateFrequency = numOperations + A[currentKey]
            if runningSum < candidateFrequency:
                if maximumFrequency < runningSum:
                    maximumFrequency = runningSum
            else:
                if maximumFrequency < candidateFrequency:
                    maximumFrequency = candidateFrequency
            pos += 1

        return maximumFrequency