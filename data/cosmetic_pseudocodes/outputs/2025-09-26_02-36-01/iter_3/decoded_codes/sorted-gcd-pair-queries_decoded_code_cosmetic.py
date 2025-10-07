from collections import Counter
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums, queries):
        topValue = max(nums) if nums else 0

        counts = Counter(nums)

        gcdCounts = [0] * (topValue + 1)

        # Inclusion-exclusion to count pairs with gcd = divisor
        for divisor in range(topValue, 0, -1):
            sumCount = 0
            multiple = divisor
            while multiple <= topValue:
                frequency = counts.get(multiple, 0)
                sumCount += frequency
                gcdCounts[divisor] -= gcdCounts[multiple]
                multiple += divisor
            pairsCount = sumCount * (sumCount - 1) // 2
            gcdCounts[divisor] += pairsCount

        prefixSums = [0]
        for i in range(1, topValue + 1):
            prefixSums.append(prefixSums[-1] + gcdCounts[i])

        answers = []
        for queryVal in queries:
            # bisect_right returns insertion point to keep prefixSums sorted;
            # we want the smallest index i where prefixSums[i] > queryVal
            pos = bisect_right(prefixSums, queryVal)
            answers.append(pos)

        return answers