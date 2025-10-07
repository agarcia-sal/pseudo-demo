from typing import List

class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        def verifyFeasibility(testVal: int, k: int) -> bool:
            active_accumulator = -1
            ops_count = 0
            index = 0
            length = len(nums)

            while index < length:
                element = nums[index]
                if active_accumulator == -1:
                    active_accumulator = element
                else:
                    active_accumulator &= element

                if (active_accumulator & testVal) == 0:
                    active_accumulator = -1
                else:
                    ops_count += 1
                    if ops_count > k:
                        return False
                index += 1
            return True

        def powerTwo(exp: int) -> int:
            resultVal = 1
            for _ in range(exp):
                resultVal <<= 1
            return resultVal

        maxInt = powerTwo(30) - 1
        accumulatorVar = maxInt
        positionVar = 0

        while positionVar < 30:
            maskVal = powerTwo(positionVar)

            if (accumulatorVar & maskVal) == 0:
                positionVar += 1
                continue

            test_condition = (~accumulatorVar) ^ maskVal
            if verifyFeasibility(test_condition, k):
                accumulatorVar &= ~maskVal

            positionVar += 1

        return accumulatorVar