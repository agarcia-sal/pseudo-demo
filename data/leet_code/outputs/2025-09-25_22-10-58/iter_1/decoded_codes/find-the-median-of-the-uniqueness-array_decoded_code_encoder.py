from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(target):
            count = 0
            left = 0
            freq = defaultdict(int)
            distinct_count = 0
            for right, num in enumerate(nums):
                if freq[num] == 0:
                    distinct_count += 1
                freq[num] += 1
                while distinct_count > target:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        distinct_count -= 1
                    left += 1
                count += right - left + 1
            return count

        n = len(nums)
        total_subarrays = n * (n + 1) // 2
        median_position = (total_subarrays + 1) // 2
        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if countLessOrEqual(mid) < median_position:
                low = mid + 1
            else:
                high = mid
        return low