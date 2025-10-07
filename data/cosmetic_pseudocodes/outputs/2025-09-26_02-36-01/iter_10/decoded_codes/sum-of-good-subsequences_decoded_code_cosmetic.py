from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        M = 10 ** 9 + 7
        freqF = defaultdict(int)
        freqG = defaultdict(int)

        def ProcessIdx(I):
            current = nums[I]

            freqG[current] = (freqG[current] + 1) % M
            freqF[current] = (freqF[current] + current) % M

            freqF[current] = (freqF[current] + freqF[current - 1] + freqG[current - 1] * current) % M
            freqG[current] = (freqG[current] + freqG[current - 1]) % M

            freqF[current] = (freqF[current] + freqF[current + 1] + freqG[current + 1] * current) % M
            freqG[current] = (freqG[current] + freqG[current + 1]) % M

        for i in range(len(nums)):
            ProcessIdx(i)

        accumulator = 0
        for val in freqF.values():
            accumulator += val

        return accumulator % M