class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        length_nums = len(nums)

        def canMakeNonDecreasing(start, length):
            amount = 0
            highest = nums[start]
            for idx in range(1, length):
                if nums[start + idx] < highest:
                    amount += highest - nums[start + idx]
                highest = max(highest, nums[start + idx])
                if amount > k:
                    return False
            return True

        all_subarrays = length_nums * (length_nums + 1) // 2
        bad_subarrays = 0
        position = 0

        while position < length_nums:
            low, high = 1, length_nums - position
            while low <= high:
                middle = (low + high) // 2
                if canMakeNonDecreasing(position, middle):
                    low = middle + 1
                else:
                    high = middle - 1
            bad_subarrays += length_nums - position - high
            position += 1

        return all_subarrays - bad_subarrays