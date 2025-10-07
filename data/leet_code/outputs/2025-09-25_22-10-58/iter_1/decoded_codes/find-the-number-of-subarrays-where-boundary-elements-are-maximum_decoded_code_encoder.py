from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums):
        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)

        count = 0
        for indices in index_map.values():
            m = len(indices)
            for i in range(m):
                for j in range(i, m):
                    subarray = nums[indices[i]: indices[j] + 1]
                    if max(subarray) == nums[indices[i]]:
                        count += 1
        return count