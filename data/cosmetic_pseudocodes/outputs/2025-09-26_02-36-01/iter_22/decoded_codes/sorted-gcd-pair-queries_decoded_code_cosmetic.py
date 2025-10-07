from collections import defaultdict
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        highest = 0
        n = len(nums)
        # Find the highest value in nums
        for num in nums:
            if num > highest:
                highest = num

        accumulator = defaultdict(int)
        for num in nums:
            accumulator[num] += 1

        distribution = [0] * (highest + 1)

        k = highest
        while k >= 1:
            tempVar = 0
            m = k
            while m <= highest:
                if m in accumulator:
                    tempVar += accumulator[m]
                distribution[k] -= distribution[m]
                m += k
            distribution[k] += tempVar * (tempVar - 1) // 2  # integer division since count is integral
            k -= 1

        prefixSum = [0] * (highest + 1)
        prefixSum[0] = distribution[0]
        for index in range(1, highest + 1):
            prefixSum[index] = prefixSum[index - 1] + distribution[index]

        output = []
        for elt in queries:
            low, high = 0, len(prefixSum)
            while low < high:
                middle = (low + high) // 2
                if prefixSum[middle] <= elt:
                    low = middle + 1
                else:
                    high = middle
            output.append(low)
        return output