from collections import Counter
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        maximum_element = max(nums) if nums else 0
        frequency_map = Counter(nums)
        gcd_counts = [0] * (maximum_element + 1)

        divisor = maximum_element
        while divisor > 0:
            temp_sum = 0
            multiple = divisor
            while multiple <= maximum_element:
                count_at_multiple = frequency_map.get(multiple, 0)
                temp_sum += count_at_multiple

                gcd_counts[divisor] -= gcd_counts[multiple]
                multiple += divisor

            # Number of pairs formed from temp_sum elements: C(temp_sum, 2) = temp_sum*(temp_sum-1)//2
            gcd_counts[divisor] += temp_sum * (temp_sum - 1) // 2
            divisor -= 1

        prefix_sums = [0] * len(gcd_counts)
        running_total = 0
        for i in range(len(gcd_counts)):
            running_total += gcd_counts[i]
            prefix_sums[i] = running_total

        def upper_bound(array: List[int], target: int) -> int:
            left, right = 0, len(array)
            while left < right:
                middle = (left + right) // 2
                if array[middle] > target:
                    right = middle
                else:
                    left = middle + 1
            return left

        answers = []
        for query_element in queries:
            position = upper_bound(prefix_sums, query_element)
            answers.append(position)

        return answers