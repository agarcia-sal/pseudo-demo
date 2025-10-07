class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        def cmpElements(a, b, c):
            # c == 1   -> b > a
            # c == 0   -> b == a
            # c == -1  -> b < a
            if c == 1:
                return b > a
            elif c == 0:
                return b == a
            elif c == -1:
                return b < a
            return False  # fallback, though not expected

        lengthNums = len(nums)
        lengthPattern = len(pattern)
        totalMatches = 0
        idxOuter = 0

        # The constraint idxOuter <= lengthNums - lengthPattern - 1
        # corresponds to ensuring nums segment from idxOuter to idxOuter + lengthPattern inclusive is valid
        # Since pattern length is lengthPattern, we check consecutive pairs from idxOuter to idxOuter + lengthPattern

        while idxOuter <= lengthNums - lengthPattern - 1:
            def innerCheck(pos, matched):
                if pos == lengthPattern:
                    return matched
                if cmpElements(nums[pos + idxOuter], nums[pos + idxOuter + 1], pattern[pos]):
                    return innerCheck(pos + 1, matched)
                return 0

            isMatchFlag = innerCheck(0, 1)
            if isMatchFlag == 1:
                totalMatches += 1
            idxOuter += 1

        return totalMatches