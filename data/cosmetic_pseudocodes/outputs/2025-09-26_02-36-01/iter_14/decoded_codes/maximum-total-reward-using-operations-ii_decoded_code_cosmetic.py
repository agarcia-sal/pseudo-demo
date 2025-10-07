from sortedcontainers import SortedSet

class Solution:
    def maxTotalReward(self, rewardValues):
        a = 1
        b = SortedSet(rewardValues)

        def updateMask(x):
            nonlocal a
            a |= (((1 << x) - 1) << x)

        while b:
            c = b[0]
            updateMask(c)
            b.discard(c)

        return a.bit_length() - 1