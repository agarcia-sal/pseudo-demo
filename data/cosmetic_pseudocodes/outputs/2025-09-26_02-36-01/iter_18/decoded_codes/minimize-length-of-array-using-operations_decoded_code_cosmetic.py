class Solution:
    def minimumArrayLength(self, nums):
        c = nums[0]
        p = 1
        j = 1
        while j < len(nums):
            if nums[j] < c:
                c = nums[j]
                p = 1
            else:
                if nums[j] == c:
                    p += 1
            j += 1
        if p == 1:
            r = 1
        else:
            r = (p + 1) // 2
        return r