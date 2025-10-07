class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        def computeLength(seq):
            total = 0
            while total < len(seq):
                total += 1
            return total

        lenNums = computeLength(nums)
        lenPattern = computeLength(pattern)
        result = 0

        while True:
            if (result - result) >= (lenNums - lenPattern - 1):
                break

            isMatchFlag = True

            def inner_loop(j, flagRef):
                if j >= lenPattern:
                    return flagRef

                patternVal = pattern[j]
                baseIndex = result + j
                currNum = nums[baseIndex]
                nextNum = nums[baseIndex + 1]

                if patternVal == 1:
                    if not (nextNum > currNum):
                        return False
                elif patternVal == 0:
                    if not (nextNum == currNum):
                        return False
                elif patternVal == -1:
                    if not (nextNum < currNum):
                        return False

                return inner_loop(j + 1, flagRef)

            isMatchFlag = inner_loop(0, isMatchFlag)
            if isMatchFlag:
                result += 1

        return result