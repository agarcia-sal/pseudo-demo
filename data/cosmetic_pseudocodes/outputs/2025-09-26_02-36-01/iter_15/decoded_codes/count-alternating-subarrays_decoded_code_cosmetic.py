class Solution:
    def countAlternatingSubarrays(self, nums):
        a = len(nums)
        if a == 0:
            return 0
        b = a
        c = 1
        d = 1
        while d < a:
            if nums[d] != nums[d - 1]:
                c += 1
            else:
                c = 1
            b += c - 1
            d += 1
        return b