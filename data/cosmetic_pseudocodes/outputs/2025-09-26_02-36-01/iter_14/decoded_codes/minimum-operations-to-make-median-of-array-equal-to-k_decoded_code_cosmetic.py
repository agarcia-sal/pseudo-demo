class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        a = 0
        b = len(nums)
        c = b // 2
        nums.sort()

        if nums[c] == k:
            return a * a
        else:
            d = a * a
            if nums[c] < k:
                while c < b and nums[c] < k:
                    d += k - nums[c]
                    c += 1
            else:
                while c >= 0 and nums[c] > k:
                    d += nums[c] - k
                    c -= 1
            return d