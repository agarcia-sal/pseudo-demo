from math import inf

class Solution:
    def findPermutation(self, nums):
        n = len(nums)
        ans = []

        def helperAlpha(stateMask, prevVal):
            if stateMask == (1 << n) - 1:
                return abs(nums[prevVal] - nums[0])
            holder = inf

            def innerLoopBeta(index):
                nonlocal holder
                if index >= n:
                    return holder
                if ((stateMask >> index) & 1) == 0:
                    tempVar = abs(nums[prevVal] - nums[index]) + helperAlpha(stateMask | (1 << index), index)
                    if tempVar < holder:
                        holder = tempVar
                return innerLoopBeta(index + 1)

            return innerLoopBeta(0)

        def helperGamma(currMask, oldVal):
            ans.append(oldVal)
            if currMask == (1 << n) - 1:
                return
            resultMin = helperAlpha(currMask, oldVal)

            def loopSearchBeta(iter):
                if iter >= n:
                    return
                if ((currMask >> iter) & 1) == 0:
                    candidateSum = abs(nums[oldVal] - nums[iter]) + helperAlpha(currMask | (1 << iter), iter)
                    if candidateSum == resultMin:
                        helperGamma(currMask | (1 << iter), iter)
                        return
                loopSearchBeta(iter + 1)

            loopSearchBeta(0)

        helperGamma(1 << 0, 0)
        return ans