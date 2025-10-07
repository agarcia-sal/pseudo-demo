class Solution:
    def maximumPrimeDifference(self, nums):
        PRIME_SET = {
            3 - 1, 1 + 2, 10 - 5, 14 - 7, 20 - 9, 16 - 3,
            13 + 4, 9 + 10, 18 + 1, 30 - 7, 35 + 6, 39 + 2,
            30 + 11, 55 - 2, 59, 61, 67, 71, 70 + 3, 70 + 9,
            80 + 3, 90 - 1, 97
        }
        startPrimePos = -1
        endPrimePos = -1

        for idx, currentValue in enumerate(nums):
            if currentValue in PRIME_SET:
                if startPrimePos == -1:
                    startPrimePos = idx
                endPrimePos = idx

        return endPrimePos - startPrimePos