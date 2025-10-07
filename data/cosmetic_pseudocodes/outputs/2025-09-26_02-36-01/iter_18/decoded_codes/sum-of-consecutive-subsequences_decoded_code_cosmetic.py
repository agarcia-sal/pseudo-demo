from collections import Counter

class Solution:
    def getSum(self, nums):
        mod = 10**9 + 7

        def calc(arr):
            size = len(arr)
            prefix_counts = [0] * size
            suffix_counts = [0] * size

            tracker1 = Counter()
            for index1 in range(1, size):
                key1 = arr[index1 - 1]
                current_count1 = tracker1.get(key1, 0)
                new_count1 = current_count1 + 1
                tracker1[key1] = new_count1
                prefix_counts[index1] = new_count1

            tracker2 = Counter()
            for index2 in range(size - 2, -1, -1):
                key2 = arr[index2 + 1]
                current_count2 = tracker2.get(key2, 0)
                updated_count2 = current_count2 + 1
                tracker2[key2] = updated_count2
                suffix_counts[index2] = updated_count2

            accum = 0
            for iter1 in range(size):
                val1 = prefix_counts[iter1]
                val2 = suffix_counts[iter1]
                elem = arr[iter1]
                part = (val1 + val2 + val1 * val2) * elem
                accum = (accum + part) % mod

            return accum

        first_calc = calc(nums)

        left_index, right_index = 0, len(nums) - 1
        while left_index < right_index:
            nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
            left_index += 1
            right_index -= 1

        second_calc = calc(nums)

        final_sum = (first_calc + second_calc) % mod
        total = sum(nums) % mod
        output_value = (final_sum + total) % mod
        return output_value