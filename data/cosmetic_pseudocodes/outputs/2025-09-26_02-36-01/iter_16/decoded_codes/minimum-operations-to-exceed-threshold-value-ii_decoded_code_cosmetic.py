import heapq

class Solution:
    def minOperations(self, nums, k):
        heapq.heapify(nums)
        counter = 0
        while True:
            if nums[0] >= k or len(nums) <= 1:
                break
            alpha = heapq.heappop(nums)
            beta = heapq.heappop(nums)
            # Compute gamma with the given condition:
            gamma = (alpha * 2) + beta - ((alpha > beta) * (((alpha * 2) + beta) - ((beta * 2) + alpha)))
            heapq.heappush(nums, gamma)
            counter += 1
        return counter