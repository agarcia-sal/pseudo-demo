from collections import defaultdict

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        modVal = 10**9 + 7
        accumResult = 0
        prefixCnt = defaultdict(int)
        suffixCnt = defaultdict(int)

        # Initialize suffixCnt with counts of nums
        for num in nums:
            suffixCnt[num] += 1

        def combin2(val):
            return val * (val - 1) // 2 if val >= 2 else 0

        accPss = 0
        accSpp = 0
        accPp = 0
        accSs = 0
        accPs = 0

        # compute accSs = sum of squares of suffixCnt values
        for v in suffixCnt.values():
            accSs += v * v

        n = len(nums)
        for pos in range(n):
            currVal = nums[pos]

            pCount = prefixCnt[currVal]
            sCount = suffixCnt[currVal]

            # Compute powers using ** not ^ (bitwise xor)
            # Update accPss
            accPss += pCount * (-(sCount**2) + ((sCount - 1)**2))
            # Update accSpp
            accSpp -= pCount**2
            # Update accSs
            accSs = accSs - (sCount**2) + ((sCount - 1)**2)
            # Update accPs
            accPs -= pCount

            suffixCnt[currVal] = sCount - 1
            sCount -= 1  # updated suffix count

            leftCount = pos
            rightCount = n - pos - 1

            # combin2 guards for negative or small inputs
            accumResult += combin2(leftCount) * combin2(rightCount)
            leftMinusP = leftCount - pCount
            rightMinusS = rightCount - sCount
            if leftMinusP < 0:
                leftMinusP = 0
            if rightMinusS < 0:
                rightMinusS = 0
            accumResult -= combin2(leftMinusP) * combin2(rightMinusS)

            adjPss = accPss - pCount * (sCount ** 2)
            adjSpp = accSpp - sCount * (pCount ** 2)
            adjPp = accPp - (pCount ** 2)
            adjSs = accSs - (sCount ** 2)
            adjPs = accPs - pCount * sCount

            pComp = leftCount - pCount
            sComp = rightCount - sCount
            if pComp < 0:
                pComp = 0
            if sComp < 0:
                sComp = 0

            accumResult -= adjPs * pCount * (rightCount - sCount)
            accumResult += adjPss * (-pCount)
            accumResult -= adjPs * sCount * (leftCount - pCount)
            accumResult += adjSpp * (-sCount)

            term1 = (adjPp - pComp) * sCount * (rightCount - sCount)
            term2 = (adjSs - sComp) * pCount * (leftCount - pCount)

            # Safe division by 2 after ensuring numerator is int
            accumResult -= term1 // 2
            accumResult -= term2 // 2

            accumResult %= modVal

            # Update accPss
            accPss += sCount * sCount
            accSpp += sCount * (-(pCount ** 2) + (pCount + 1) ** 2)
            accPp += (-(pCount ** 2) + (pCount + 1) ** 2)
            accPs += sCount

            prefixCnt[currVal] = pCount + 1

        return accumResult % modVal