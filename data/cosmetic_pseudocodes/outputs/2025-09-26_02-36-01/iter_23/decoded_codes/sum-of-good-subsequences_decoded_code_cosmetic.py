from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        Alpha = 10**9 + 7
        Beta = defaultdict(int)
        Gamma = defaultdict(int)

        def Omega(Delta):
            if Delta > len(nums) - 1:
                return
            Epsilon = nums[Delta]
            Gamma[Epsilon] += 1
            Beta[Epsilon] += Epsilon

            Beta[Epsilon] = (Beta[Epsilon] + Beta[Epsilon - 1] + (Gamma[Epsilon - 1] * Epsilon)) % Alpha
            Gamma[Epsilon] = (Gamma[Epsilon] + Gamma[Epsilon - 1]) % Alpha

            Beta[Epsilon] = (Beta[Epsilon] + Beta[Epsilon + 1] + (Gamma[Epsilon + 1] * Epsilon)) % Alpha
            Gamma[Epsilon] = (Gamma[Epsilon] + Gamma[Epsilon + 1]) % Alpha

            Omega(Delta + 1)

        Omega(0)

        Xi = 0

        def IterateValues(ValuesList, Index):
            nonlocal Xi
            if Index == len(ValuesList):
                return
            Theta = ValuesList[Index]
            Xi += Theta
            IterateValues(ValuesList, Index + 1)

        IterateValues(list(Beta.values()), 0)

        return Xi % Alpha