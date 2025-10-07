import heapq

class Solution:
    def minOperations(self, nums, k):
        operations = 0
        heapq.heapify(nums)
        while nums and nums[0] < k and len(nums) > 1:
            first_element = heapq.heappop(nums)
            second_element = heapq.heappop(nums)
            combined = 2 * min(first_element, second_element) + max(first_element, second_element)
            heapq.heappush(nums, combined)
            operations += 1
        return operations