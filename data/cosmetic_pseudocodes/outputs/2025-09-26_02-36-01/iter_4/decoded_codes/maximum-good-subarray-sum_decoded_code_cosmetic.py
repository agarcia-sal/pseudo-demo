class Solution:
    def maximumSubarraySum(self, nums, k):
        prefix_min_map = {}
        max_value = float('-inf')
        running_total = 0

        for element in nums:
            if (element - k) in prefix_min_map:
                candidate1 = running_total - prefix_min_map[element - k] + element
                if candidate1 > max_value:
                    max_value = candidate1
            if (element + k) in prefix_min_map:
                candidate2 = running_total - prefix_min_map[element + k] + element
                if candidate2 > max_value:
                    max_value = candidate2
            if element in prefix_min_map:
                if running_total < prefix_min_map[element]:
                    prefix_min_map[element] = running_total
            else:
                prefix_min_map[element] = running_total
            running_total += element

        return max_value if max_value != float('-inf') else 0