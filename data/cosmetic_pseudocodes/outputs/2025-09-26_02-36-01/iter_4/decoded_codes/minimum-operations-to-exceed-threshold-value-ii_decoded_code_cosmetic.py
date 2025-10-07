import heapq

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while nums and nums[0] < k and len(nums) > 1:
            first_element = heapq.heappop(nums)
            second_element = heapq.heappop(nums)
            smaller_value = first_element if first_element < second_element else second_element
            larger_value = first_element if first_element > second_element else second_element
            combined_value = smaller_value * 2 + larger_value
            heapq.heappush(nums, combined_value)
            count += 1
        return count