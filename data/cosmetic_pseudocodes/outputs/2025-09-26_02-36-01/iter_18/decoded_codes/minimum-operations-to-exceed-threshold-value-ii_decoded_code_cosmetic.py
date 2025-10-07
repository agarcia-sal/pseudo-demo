import heapq

class Solution:
    def minOperations(self, nums, k):
        heapq.heapify(nums)
        count = 0
        while True:
            if not (nums[0] < k and len(nums) > 1):
                break
            alpha = heapq.heappop(nums)
            beta = heapq.heappop(nums)
            temp_Val = min(beta, alpha) * 2 + max(beta, alpha)
            heapq.heappush(nums, temp_Val)
            count += 1
        return count