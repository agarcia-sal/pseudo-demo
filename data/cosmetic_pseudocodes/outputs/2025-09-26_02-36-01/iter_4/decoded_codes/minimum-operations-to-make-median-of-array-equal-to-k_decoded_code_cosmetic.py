class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        nums.sort()
        length_of_list = len(nums)
        mid_pos = length_of_list // 2

        if nums[mid_pos] == k:
            return 0

        total_operations = 0

        if nums[mid_pos] < k:
            idx = mid_pos
            while idx < length_of_list and nums[idx] < k:
                total_operations += k - nums[idx]
                idx += 1
        else:
            j = mid_pos
            while j >= 0 and nums[j] > k:
                total_operations += nums[j] - k
                j -= 1

        return total_operations