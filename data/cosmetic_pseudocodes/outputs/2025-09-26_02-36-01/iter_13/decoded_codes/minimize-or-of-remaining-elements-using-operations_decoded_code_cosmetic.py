class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or, k):
            sentinel = -1

            def helper(index, current_val, count_ops):
                if current_val == sentinel:
                    next_val = nums[index]
                else:
                    next_val = current_val & nums[index]

                if (next_val & target_or) == 0:
                    next_val = sentinel
                else:
                    count_ops += 1
                    if count_ops > k:
                        return False

                if index + 1 == len(nums):
                    return True
                else:
                    return helper(index + 1, next_val, count_ops)

            return helper(0, sentinel, 0)

        upper_limit = (1 << 30) - 1
        result = upper_limit

        for bit_index in range(30):
            mask = 1 << bit_index
            if (result & mask) != 0:
                def helperCanAchieve(res, mask, k):
                    return canAchieve((~res) ^ mask, k)
                if helperCanAchieve(result, mask, k):
                    result &= ~mask

        return result