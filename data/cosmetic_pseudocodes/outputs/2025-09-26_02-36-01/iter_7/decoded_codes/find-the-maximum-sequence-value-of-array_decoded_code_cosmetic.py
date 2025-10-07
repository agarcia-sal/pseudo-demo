class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        expVal = (1 << 5) << 2  # 2^(5+2) = 2^7 = 128
        lengthNums = len(nums)

        # Initialize dpForward: dimensions (lengthNums+1) x (k+2) x expVal, filled with False
        # Using lists of lists of bitarrays (boolean lists) might be too large; use list of sets for active masks
        dpForward = [ [set() for _ in range(k + 2)] for _ in range(lengthNums + 1) ]
        dpForward[0][0].add(0)

        for indexI in range(lengthNums):
            for indexJ in range(k + 1):
                for mask in dpForward[indexI][indexJ]:
                    # Not take nums[indexI]
                    dpForward[indexI + 1][indexJ].add(mask)
                    # Take nums[indexI]
                    orMask = mask | nums[indexI]
                    dpForward[indexI + 1][indexJ + 1].add(orMask)

        dpBackward = [ [set() for _ in range(k + 2)] for _ in range(lengthNums + 1) ]
        dpBackward[lengthNums][0].add(0)

        for idxI in range(lengthNums, 0, -1):
            for idxJ in range(k + 1):
                for mask in dpBackward[idxI][idxJ]:
                    # Not take nums[idxI - 1]
                    dpBackward[idxI - 1][idxJ].add(mask)
                    # Take nums[idxI - 1]
                    combinedMask = mask | nums[idxI - 1]
                    dpBackward[idxI - 1][idxJ + 1].add(combinedMask)

        result = 0
        # iterI from k to lengthNums - k incl.
        for iterI in range(k, lengthNums - k + 1):
            forward_masks = dpForward[iterI][k]
            backward_masks = dpBackward[iterI][k]
            for maskX in forward_masks:
                for maskY in backward_masks:
                    candidateVal = maskX ^ maskY
                    if candidateVal > result:
                        result = candidateVal
        return result