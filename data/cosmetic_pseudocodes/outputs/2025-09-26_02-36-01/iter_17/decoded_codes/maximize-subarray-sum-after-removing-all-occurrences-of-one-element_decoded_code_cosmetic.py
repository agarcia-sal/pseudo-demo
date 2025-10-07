class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            a = arr[0]
            b = arr[0]
            i = 1
            while i < len(arr):
                c = arr[i]
                if c > a + c:
                    a = c
                else:
                    a = a + c
                if b < a:
                    b = a
                i += 1
            return b

        d = kadane(nums)
        e = set()
        f = 0
        while f < len(nums):
            e |= {nums[f]}
            f += 1

        for g in e:
            h = []
            j = 0
            while j < len(nums):
                if nums[j] != g:
                    h.append(nums[j])
                j += 1
            if len(h) > 0:
                k = kadane(h)
                if d < k:
                    d = k

        return d