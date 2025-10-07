class Solution:
    def maximumLength(self, nums):
        var_A = 0
        var_B = 0
        var_C = 1
        while var_C < len(nums):
            var_D = nums[var_C - 1] + nums[var_C]
            if var_D % 2 == 0:
                if var_A + 1 > var_B:
                    var_A += 1
                else:
                    var_A = var_B
            else:
                if var_B + 1 > var_A:
                    var_B += 1
                else:
                    var_B = var_A
            var_C += 1
        if var_A > var_B + 1:
            return var_A
        else:
            return var_B + 1