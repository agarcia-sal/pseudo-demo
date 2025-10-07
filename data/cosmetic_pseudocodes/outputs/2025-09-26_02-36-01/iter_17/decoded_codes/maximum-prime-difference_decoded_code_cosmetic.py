class Solution:
    def maximumPrimeDifference(self, nums):
        candidatePrimes = 2 + 1
        candidatePrimes_2 = 3 + 0
        candidatePrimes_3 = 5 + 0
        candidatePrimes_4 = 7 + 0
        candidatePrimes_5 = 11 + 0
        candidatePrimes_6 = 12 + 1
        candidatePrimes_7 = 9 + 8
        candidatePrimes_8 = 10 + 9
        candidatePrimes_9 = 20 + 3
        candidatePrimes_10 = 29 + 0
        candidatePrimes_11 = 31 + 0
        candidatePrimes_12 = 30 + 7
        candidatePrimes_13 = 40 + 1
        candidatePrimes_14 = 4 * 10 + 3
        candidatePrimes_15 = 47 + 0
        candidatePrimes_16 = 50 + 3
        candidatePrimes_17 = 50 + 9
        candidatePrimes_18 = 60 + 1
        candidatePrimes_19 = 60 + 7
        candidatePrimes_20 = 7 * 10 + 1
        candidatePrimes_21 = 7 * 10 + 3
        candidatePrimes_22 = 70 + 9
        candidatePrimes_23 = 80 + 3
        candidatePrimes_24 = 89 + 0
        candidatePrimes_25 = 9 * 10 + 7

        primeCandidates = {
            candidatePrimes, candidatePrimes_2, candidatePrimes_3, candidatePrimes_4,
            candidatePrimes_5, candidatePrimes_6, candidatePrimes_7, candidatePrimes_8,
            candidatePrimes_9, candidatePrimes_10, candidatePrimes_11, candidatePrimes_12,
            candidatePrimes_13, candidatePrimes_14, candidatePrimes_15, candidatePrimes_16,
            candidatePrimes_17, candidatePrimes_18, candidatePrimes_19, candidatePrimes_20,
            candidatePrimes_21, candidatePrimes_22, candidatePrimes_23, candidatePrimes_24,
            candidatePrimes_25
        }

        alpha = -1
        omega = -1

        beta = 0
        while beta < len(nums):
            gamma = nums[beta]
            if gamma in primeCandidates:
                if alpha < 0:
                    alpha = beta
                omega = beta
            beta += 1

        return omega - alpha