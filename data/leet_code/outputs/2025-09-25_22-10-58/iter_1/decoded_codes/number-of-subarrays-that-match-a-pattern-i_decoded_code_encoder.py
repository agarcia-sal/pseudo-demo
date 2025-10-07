class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        n = len(nums)
        m = len(pattern)
        count = 0
        for i in range(n - m):
            match = True
            for k in range(m):
                if pattern[k] == 1:
                    if nums[i + k + 1] <= nums[i + k]:
                        match = False
                        break
                elif pattern[k] == 0:
                    if nums[i + k + 1] != nums[i + k]:
                        match = False
                        break
                elif pattern[k] == -1:
                    if nums[i + k + 1] >= nums[i + k]:
                        match = False
                        break
            if match:
                count += 1
        return count