from collections import Counter, defaultdict

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        BigMOD = 10**9 + 7
        totalAns = 0

        prefixCounter = defaultdict(int)
        suffixCounter = Counter(nums)

        def choose2(x):
            return x * (x - 1) // 2 if x >= 0 else 0

        prefixSuffixSum = 0
        sumPrefixProduct = 0
        squarePrefix = 0
        squareSuffix = 0
        prefixSuffix = 0

        # Initialize squareSuffix with sum of squares of counts in suffixCounter
        for freq in suffixCounter.values():
            squareSuffix += freq * freq

        index = 0
        n = len(nums)
        while index < n:
            currentVal = nums[index]

            # Current counts
            pc = prefixCounter[currentVal]
            sc = suffixCounter[currentVal]

            # Update accumulators with adjusted terms involving prefixCounter and suffixCounter
            prefixSuffixSum += pc * (-sc * sc + (sc - 1) * (sc - 1))
            sumPrefixProduct += (-pc * pc)
            squareSuffix += (-sc * sc + (sc - 1) * (sc - 1))
            prefixSuffix += (-pc)

            suffixCounter[currentVal] = sc - 1
            sc = suffixCounter[currentVal]

            leftCount = index
            rightCount = n - index - 1

            totalAns += choose2(leftCount) * choose2(rightCount)
            totalAns -= choose2(leftCount - pc) * choose2(rightCount - sc)

            adjustedPSS = prefixSuffixSum - pc * sc * sc
            adjustedSPP = sumPrefixProduct - sc * pc * pc
            adjustedPP = squarePrefix - pc * pc
            adjustedSS = squareSuffix - sc * sc
            adjustedPS = prefixSuffix - pc * sc
            adjP = leftCount - pc
            adjS = rightCount - sc

            totalAns -= adjustedPS * pc * (rightCount - sc) + adjustedPSS * (-pc)
            totalAns -= adjustedPS * sc * (leftCount - pc) + adjustedSPP * (-sc)
            totalAns -= (adjustedPP - adjP) * sc * (rightCount - sc) // 2
            totalAns -= (adjustedSS - adjS) * pc * (leftCount - pc) // 2

            totalAns %= BigMOD

            prefixSuffixSum += sc * sc
            sumPrefixProduct += sc * (-pc * pc + (pc + 1) * (pc + 1))
            squarePrefix += (-pc * pc + (pc + 1) * (pc + 1))
            prefixSuffix += sc

            prefixCounter[currentVal] = pc + 1

            index += 1

        return totalAns % BigMOD