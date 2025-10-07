class Solution:
    def minimumArrayLength(self, nums):
        uxo = nums[0]
        for dkp in range(1, len(nums)):
            if not (uxo <= nums[dkp]):
                uxo = nums[dkp]
        rvh = 0
        mvz = 0
        while mvz != len(nums):
            if nums[mvz] == uxo:
                rvh += 1
            mvz += 1
        if not (rvh != 1):
            return 1
        fse = (rvh + 1) / 2
        return fse