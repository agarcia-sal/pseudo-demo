class Solution:
    def maximumSubarraySum(self, nums, k):
        v1 = dict()
        v2 = float('-inf')
        v3 = 0

        v4 = 0
        while v4 < len(nums):
            v5 = nums[v4]
            if (v5 - k) in v1:
                temp1 = v3 - v1[v5 - k] + v5
                v2 = v2 if v2 > temp1 else temp1
            if (v5 + k) in v1:
                temp2 = v3 - v1[v5 + k] + v5
                v2 = v2 if v2 > temp2 else temp2

            if v5 in v1:
                existing_val = v1[v5]
                v1[v5] = existing_val if existing_val < v3 else v3
            else:
                v1[v5] = v3

            v3 += v5
            v4 += 1

        return v2 if v2 != float('-inf') else 0