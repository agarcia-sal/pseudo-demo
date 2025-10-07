from collections import Counter, defaultdict

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MODULO_VALUE = 10**9 + 7
        totalCount = 0
        prefixCount = defaultdict(int)
        suffixCount = Counter(nums)

        def choose2(x):
            return (x * (x - 1)) // 2 if x >= 0 else 0

        prefixSuffixSum = 0
        suffixPrefixProduct = 0
        prefixPrefixProduct = 0
        suffixSquaredSum = 0
        for val in suffixCount.values():
            suffixSquaredSum += val * val
        prefixSuffixSumAlt = 0

        n = len(nums)
        index = 0
        while index < n:
            currentElement = nums[index]

            pc = prefixCount[currentElement]
            sc = suffixCount[currentElement]

            prefixSuffixSum += pc * (-(sc * sc) + (sc - 1) * (sc - 1))
            suffixPrefixProduct += -pc * pc
            suffixSquaredSum += (-(sc * sc) + (sc - 1) * (sc - 1))
            prefixSuffixSumAlt += -pc

            suffixCount[currentElement] = sc - 1

            leftCount = index
            rightCount = n - 1 - index

            totalCount += choose2(leftCount) * choose2(rightCount)
            totalCount -= choose2(leftCount - pc) * choose2(rightCount - suffixCount[currentElement])

            pc_new = pc
            sc_new = suffixCount[currentElement]

            prefixSuffixReduced = prefixSuffixSum - pc_new * (sc_new * sc_new)
            suffixPrefixProductReduced = suffixPrefixProduct - sc_new * (pc_new * pc_new)
            prefixPrefixProductReduced = prefixPrefixProduct - pc_new * pc_new
            suffixSquaredSumReduced = suffixSquaredSum - sc_new * sc_new
            prefixSuffixSumAltReduced = prefixSuffixSumAlt - pc_new * sc_new

            prefixRemaining = leftCount - pc_new
            suffixRemaining = rightCount - sc_new

            totalCount -= prefixSuffixSumAltReduced * pc_new * suffixRemaining
            totalCount -= prefixSuffixReduced * (-pc_new)
            totalCount -= prefixSuffixSumAltReduced * sc_new * prefixRemaining
            totalCount -= suffixPrefixProductReduced * (-sc_new)
            totalCount -= (prefixPrefixProductReduced - prefixRemaining) * sc_new * suffixRemaining / 2
            totalCount -= (suffixSquaredSumReduced - suffixRemaining) * pc_new * prefixRemaining / 2

            totalCount %= MODULO_VALUE

            prefixSuffixSum += sc_new * sc_new
            suffixPrefixProduct += sc_new * (-(pc_new * pc_new)) + (pc_new + 1) * (pc_new + 1)
            prefixPrefixProduct += -(pc_new * pc_new) + (pc_new + 1) * (pc_new + 1)
            prefixSuffixSumAlt += sc_new

            prefixCount[currentElement] = pc_new + 1

            index += 1

        return totalCount % MODULO_VALUE