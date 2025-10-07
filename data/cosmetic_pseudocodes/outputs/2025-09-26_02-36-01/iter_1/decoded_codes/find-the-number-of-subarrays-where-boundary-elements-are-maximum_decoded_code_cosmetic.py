from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums):
        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)

        total_count = 0

        for indices in index_map.values():
            size = len(indices)
            for start_pos in range(size):
                for end_pos in range(start_pos, size):
                    left_idx = indices[start_pos]
                    right_idx = indices[end_pos]
                    segment = nums[left_idx:right_idx + 1]
                    max_in_segment = max(segment)
                    if max_in_segment == nums[left_idx]:
                        total_count += 1

        return total_count