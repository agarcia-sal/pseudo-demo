class Solution:
    def countOfPairs(self, nums):
        MOD = 1_000_000_007
        n = len(nums)
        max_num = max(nums)

        def initialize3DArray(x, y, z):
            def create2DArray(a, b):
                def create1DArray(size):
                    return [0] * size
                return [create1DArray(b) for _ in range(a)]
            return [create2DArray(y, z) for _ in range(x)]

        tempDP = initialize3DArray(n + 1, max_num + 1, max_num + 1)

        firstNum = nums[0]
        for varI in range(firstNum + 1):
            tempDP[1][varI][firstNum - varI] = 1

        def sumModulo(a, b, modVal):
            return (a + b) % modVal

        def isEqual(a, b):
            return a == b

        for outerIndex in range(2, n + 1):
            val = nums[outerIndex - 1]
            for middleIndex in range(val + 1):
                for innerIndex in range(val + 1):
                    if isEqual(middleIndex + innerIndex, val):
                        acc = 0
                        prev_j_limit = middleIndex + 1
                        prev_k_start = innerIndex
                        prev_k_limit = max_num + 1
                        dp_outer = tempDP[outerIndex][middleIndex]
                        dp_prev = tempDP[outerIndex - 1]
                        for prevJIndex in range(prev_j_limit):
                            prevJ_row = dp_prev[prevJIndex]
                            for prevKIndex in range(prev_k_start, prev_k_limit):
                                dp_outer[innerIndex] = sumModulo(dp_outer[innerIndex], prevJ_row[prevKIndex], MOD)
                                # accumulate in dp_outer[innerIndex], corrected threshold below

                        # The above line incorrectly sums all prevKIndex values for a fixed innerIndex only.
                        # Actually, we need to accumulate over prevKIndex as the third dimension:
                        # That is, tempDP[outerIndex][middleIndex][innerIndex] += tempDP[outerIndex - 1][prevJIndex][prevKIndex]
                        # So summation over prevKIndex s are added for fixed innerIndex.

                        # Fix data assignment:
                        # Reset dp_outer[innerIndex] to 0 before accumulation:
                        dp_outer[innerIndex] = 0
                        for prevJIndex in range(prev_j_limit):
                            prevJ_row = dp_prev[prevJIndex]
                            for prevKIndex in range(prev_k_start, prev_k_limit):
                                dp_outer[innerIndex] = sumModulo(dp_outer[innerIndex], prevJ_row[prevKIndex], MOD)

        finalResult = 0
        for posJ in range(max_num + 1):
            for posK in range(max_num + 1):
                finalResult = sumModulo(finalResult, tempDP[n][posJ][posK], MOD)

        return finalResult