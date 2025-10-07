import heapq

class Solution:
    def minOperations(self, nums, k):
        heapq.heapify(nums)
        counter = 0
        while (len(nums) > 1 and nums[0] < k):
            temp1 = heapq.heappop(nums)
            temp2 = heapq.heappop(nums)
            combined = max(temp1, temp2) + min(temp1, temp2) * 2
            heapq.heappush(nums, combined)
            counter += 1
        return counter