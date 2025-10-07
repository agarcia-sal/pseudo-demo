class Solution:
    def maximumValueSum(self, nums, k, edges=None):
        # edges parameter unused as per pseudocode

        accumulator = 0
        counter_odd_gains = 0
        minimal_gain_value = float('inf')

        def absVal(x):
            return -x if x < 0 else x

        def maxVal(x, y):
            return x if x > y else y

        def minVal(x, y):
            return x if x < y else y

        def xorOp(a, b):
            return a ^ b

        def loopAt(index):
            nonlocal accumulator, counter_odd_gains, minimal_gain_value
            if index >= len(nums):
                return
            number = nums[index]
            computed_xor = xorOp(number, k)
            difference = computed_xor - number
            if difference > 0:
                counter_odd_gains += 1
            accumulator += maxVal(number, computed_xor)
            minimal_gain_value = minVal(minimal_gain_value, absVal(difference))
            loopAt(index + 1)

        loopAt(0)
        if counter_odd_gains % 2 != 0:
            accumulator -= minimal_gain_value
        return accumulator