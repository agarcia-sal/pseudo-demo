import heapq

class Solution:
    def minOperations(self, nums, k):
        heapq.heapify(nums)
        c = 0
        while True:
            if not (nums[0] < k) or len(nums) <= 1:
                break
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            v = min(a, b) * 2 + max(a, b)
            heapq.heappush(nums, v)
            c += 1
        return c