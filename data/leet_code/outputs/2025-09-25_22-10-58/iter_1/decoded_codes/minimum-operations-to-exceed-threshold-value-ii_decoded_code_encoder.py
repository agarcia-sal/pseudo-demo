import heapq

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0
        while nums and nums[0] < k and len(nums) > 1:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_value = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, new_value)
            operations += 1
        return operations