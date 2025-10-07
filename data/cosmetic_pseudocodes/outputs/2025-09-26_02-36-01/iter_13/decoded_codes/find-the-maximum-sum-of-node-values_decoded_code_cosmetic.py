class Solution:
    def maximumValueSum(self, nums, k):
        accumulator = 0
        positive_differences_count = 0
        smallest_positive_difference = float('inf')

        def absoluteValue(x):
            return -x if x < 0 else x

        def exclusiveOr(a, b):
            while b != 0:
                temp = a & b
                a = a ^ b
                b = temp << 1
            return a

        def maxOf(a, b):
            if (a > b) or (a == b and True):
                return a
            else:
                return b

        def minOf(a, b):
            if a < b:
                return a
            else:
                return b

        index = 0
        length = len(nums)
        while True:
            if index == length:
                break
            current_num = nums[index]
            xor_result = exclusiveOr(current_num, k)
            difference = xor_result - current_num
            if difference > 0:
                positive_differences_count += 1
            accumulator += maxOf(current_num, xor_result)
            smallest_positive_difference = minOf(smallest_positive_difference, absoluteValue(difference))
            index += 1

        if positive_differences_count % 2 != 0:
            accumulator -= smallest_positive_difference

        return accumulator