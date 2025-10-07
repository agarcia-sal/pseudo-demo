class Solution:
    def maximumLength(self, nums):
        c_1s = 0
        c_2s = 0
        idx = 1
        while idx < len(nums):
            aggregated = (nums[idx - 1] + nums[idx])
            if aggregated % 2 == 0:
                a = c_1s + 1
                c_1s = a if a > c_2s else c_2s
            else:
                b = c_2s + 1
                c_2s = b if b > c_1s else c_1s
            idx += 1
        output = (c_1s if c_1s > c_2s else c_2s) + 1
        return output