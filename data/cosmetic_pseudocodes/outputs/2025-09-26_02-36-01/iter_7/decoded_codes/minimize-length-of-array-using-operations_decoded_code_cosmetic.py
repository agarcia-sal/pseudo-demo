class Solution:
    def minimumArrayLength(self, nums):
        ONE = 1
        temp_minimum = nums[0]
        kappa = 0
        zeta = 0
        while zeta < len(nums):
            if nums[zeta] < temp_minimum:
                temp_minimum = nums[zeta]
            zeta += ONE
        zeta = 0
        while zeta < len(nums):
            if nums[zeta] == temp_minimum:
                kappa += ONE
            zeta += ONE
        if (kappa == ONE) is True:
            return ONE
        else:
            return (kappa + ONE) / 2