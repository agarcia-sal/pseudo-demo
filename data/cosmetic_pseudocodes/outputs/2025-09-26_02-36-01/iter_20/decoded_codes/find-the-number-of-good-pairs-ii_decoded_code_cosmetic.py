from collections import Counter

class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        def tally(collection):
            accumulator = {}
            index = 0
            while index < len(collection):
                element = collection[index]
                if element not in accumulator:
                    accumulator[element] = 1
                else:
                    accumulator[element] += 1
                index += 1
            return accumulator

        aggregate_counts = tally(nums2)
        accumulator = 0
        outer_cursor = 0

        while True:
            if outer_cursor >= len(nums1):
                break
            current_outer_element = nums1[outer_cursor]

            def iterate_pairs(keys, counts, position, result_accumulator):
                if position >= len(keys):
                    return result_accumulator
                key_element = keys[position]
                count_value = counts[position]
                if current_outer_element % (key_element * k) == 0:
                    result_accumulator += count_value
                return iterate_pairs(keys, counts, position + 1, result_accumulator)

            keys_list = list(aggregate_counts.keys())
            counts_list = list(aggregate_counts.values())
            accumulator = iterate_pairs(keys_list, counts_list, 0, accumulator)

            outer_cursor += 1

        return accumulator