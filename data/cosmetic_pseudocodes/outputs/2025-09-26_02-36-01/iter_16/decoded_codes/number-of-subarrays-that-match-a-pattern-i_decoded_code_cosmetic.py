class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        n = len(nums)
        m = len(pattern)
        count = 0
        i = 0
        while i <= n - m:
            match = True
            j = 0
            while match and j < m - 1:
                cond_val = (pattern[j] - 1) * (nums[i + j + 1] - nums[i + j])
                # If cond_val >= 0 and pattern[j] != 1, proceed with checks
                if cond_val >= 0 and pattern[j] != 1:
                    if pattern[j] == 1:
                        if nums[i + j + 1] <= nums[i + j]:
                            match = False
                            break
                    elif pattern[j] == 0:
                        if nums[i + j + 1] != nums[i + j]:
                            match = False
                            break
                    elif pattern[j] == -1:
                        if nums[i + j + 1] >= nums[i + j]:
                            match = False
                            break
                j += 1
            if match:
                count += 1
            i += 1
        return count