import heapq

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        op_count = 0
        while len(nums) > 1 and nums[0] < k:
            first_min = heapq.heappop(nums)
            second_min = heapq.heappop(nums)

            # The following is the translation of the logic in pseudocode:
            # The code has multiple reassignments for combined that overwrite each other,
            # so the last condition determines combined:
            # If first_min < second_min, combined = 2*first_min + second_min
            # Else combined = 2*second_min + first_min

            if first_min < second_min:
                combined = 2 * first_min + second_min
            else:
                combined = 2 * second_min + first_min

            heapq.heappush(nums, combined)
            op_count += 1

        return op_count