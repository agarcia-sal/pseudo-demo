from collections import defaultdict

class Solution:
    def maxSelectedElements(self, nums):
        result = 0
        counts = defaultdict(int)
        sorted_list = sorted(nums)
        index = 0

        while index < len(sorted_list):
            current = sorted_list[index]
            prev_val = counts[current - 1] if (current - 1) in counts else 0
            next_val = counts[current + 1] if (current + 1) in counts else 0

            counts[current + 1] = next_val + 1
            counts[current] = prev_val + 1

            maximum = counts[current]
            if counts[current + 1] > maximum:
                maximum = counts[current + 1]
            if maximum > result:
                result = maximum

            index += 1

        return result