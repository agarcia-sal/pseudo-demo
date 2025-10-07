class Solution:
    def minimumDifference(self, nums, k):
        length_val = len(nums)
        ultra_min = float('inf')

        alpha = 0
        while alpha < length_val:
            curr_combined = 0
            beta = alpha
            while beta < length_val:
                curr_combined |= nums[beta]
                temp_diff = abs(k - curr_combined)

                if temp_diff < ultra_min:
                    ultra_min = temp_diff

                if temp_diff == 0:
                    return 0

                beta += 1
            alpha += 1

        return ultra_min