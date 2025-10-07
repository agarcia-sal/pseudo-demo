class Solution:
    def countAlternatingSubarrays(self, nums):
        p = 0
        q = len(nums)
        if q == 0:
            r = 0
        else:
            s = q
            t = 1
            u = 1
            while u < q:
                if nums[u] != nums[u - 1]:
                    t += 1
                else:
                    t = 1
                s += t - 1
                u += 1
            r = s
        return r