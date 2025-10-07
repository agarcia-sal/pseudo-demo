from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        BASE = 10**9 + 7

        def combin2(x):
            return x * (x - 1) // 2 if x >= 2 else 0

        total_result = 0
        prefixCounts = Counter()
        suffixCounts = Counter(nums)

        prefixSuffixSum = 0
        suffixPrefixProduct = 0
        prefixPrefixSum = 0
        suffixSumSquares = 0
        prefixSuffixProduct = 0

        for val, freq in suffixCounts.items():
            suffixSumSquares += freq * freq

        n = len(nums)
        for index in range(n):
            currentElement = nums[index]

            pc = prefixCounts[currentElement]
            sc = suffixCounts[currentElement]

            prefixSuffixSum += pc * (- (sc * sc) + (sc - 1) * (sc - 1))
            suffixPrefixProduct += - (pc * pc)
            suffixSumSquares += - (sc * sc) + (sc - 1) * (sc - 1)
            prefixSuffixProduct += - pc

            suffixCounts[currentElement] = sc - 1
            sc -= 1  # update sc for further calculations

            leftLength = index
            rightLength = n - index - 1

            total_result += combin2(leftLength) * combin2(rightLength)

            adjustedLeft = leftLength - pc
            adjustedRight = rightLength - sc
            total_result -= combin2(adjustedLeft) * combin2(adjustedRight)

            prefixSuffixSumAdj = prefixSuffixSum - pc * (sc * sc)
            suffixPrefixProductAdj = suffixPrefixProduct - sc * (pc * pc)
            prefixPrefixSumAdj = prefixPrefixSum - (pc * pc)
            suffixSumSquaresAdj = suffixSumSquares - (sc * sc)
            prefixSuffixProductAdj = prefixSuffixProduct - pc * sc

            prefixDiff = leftLength - pc
            suffixDiff = rightLength - sc

            decrementVal1 = prefixSuffixProductAdj * pc * (rightLength - sc) + prefixSuffixSumAdj * (-pc)
            decrementVal2 = prefixSuffixProductAdj * sc * (leftLength - pc) + suffixPrefixProductAdj * (-sc)
            decrementVal3 = ((prefixPrefixSumAdj - prefixDiff) * sc * (rightLength - sc)) // 2
            decrementVal4 = ((suffixSumSquaresAdj - suffixDiff) * pc * (leftLength - pc)) // 2

            total_result -= decrementVal1
            total_result -= decrementVal2
            total_result -= decrementVal3
            total_result -= decrementVal4

            total_result %= BASE

            prefixSuffixSum += sc * sc
            suffixPrefixProduct += sc * (- (pc * pc) + (pc + 1) * (pc + 1))
            prefixPrefixSum += - (pc * pc) + (pc + 1) * (pc + 1)
            prefixSuffixProduct += sc

            prefixCounts[currentElement] = pc + 1

        return total_result % BASE