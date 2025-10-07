from collections import Counter, defaultdict

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MODULO = 10**9 + 7

        def combinationTwo(x):
            return x * (x - 1) // 2 if x >= 2 else 0

        answer = 0
        prefixCount = defaultdict(int)
        suffixCount = Counter(nums)

        prefixSuffixSum = 0
        suffixPrefixProduct = 0
        prefixSquareSum = 0
        suffixSquareSum = sum(v * v for v in suffixCount.values())
        prefixSuffixSumBasic = 0

        n = len(nums)

        for index in range(n):
            current = nums[index]

            c_prefix = prefixCount[current]
            c_suffix = suffixCount[current]

            # Update prefixSuffixSum before suffixCount decreases
            prefixSuffixSum += c_prefix * (-(c_suffix ** 2) + ((c_suffix - 1) ** 2))
            suffixPrefixProduct += -(c_prefix ** 2)
            suffixSquareSum += -(c_suffix ** 2) + ((c_suffix - 1) ** 2)
            prefixSuffixSumBasic += - c_prefix

            suffixCount[current] = c_suffix - 1

            leftLength = index
            rightLength = n - index - 1

            answer += combinationTwo(leftLength) * combinationTwo(rightLength)
            answer -= combinationTwo(leftLength - c_prefix) * combinationTwo(rightLength - (c_suffix - 1))

            psSumAdjusted = prefixSuffixSum - c_prefix * (c_suffix ** 2)
            spProductAdjusted = suffixPrefixProduct - (c_suffix - 1) * (c_prefix ** 2)
            prefixSquareAdjusted = prefixSquareSum - (c_prefix ** 2)
            suffixSquareAdjusted = suffixSquareSum - ((c_suffix - 1) ** 2)
            psBasicAdjusted = prefixSuffixSumBasic - c_prefix * (c_suffix - 1)

            prefixRemain = leftLength - c_prefix
            suffixRemain = rightLength - (c_suffix - 1)

            term1 = psBasicAdjusted * c_prefix * suffixRemain + psSumAdjusted * (-c_prefix)
            term2 = psBasicAdjusted * (c_suffix - 1) * prefixRemain + spProductAdjusted * (-(c_suffix - 1))
            term3 = (prefixSquareAdjusted - prefixRemain) * (c_suffix - 1) * suffixRemain // 2
            term4 = (suffixSquareAdjusted - suffixRemain) * c_prefix * prefixRemain // 2

            answer -= term1 + term2 + term3 + term4

            answer %= MODULO

            # Update prefixSuffixSum and others after prefixCount increases
            prefixSuffixSum += (c_suffix - 1) ** 2
            suffixPrefixProduct += (c_suffix - 1) * ( - (c_prefix ** 2) + (c_prefix + 1) ** 2)
            prefixSquareSum += - (c_prefix ** 2) + (c_prefix + 1) ** 2
            prefixSuffixSumBasic += (c_suffix - 1)

            prefixCount[current] = c_prefix + 1

        return answer % MODULO