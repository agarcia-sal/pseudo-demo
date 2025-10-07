class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        mapping_freqs = {}
        for val in nums2:
            mapping_freqs[val] = mapping_freqs.get(val, 0) + 1

        total_good_pairs = 0
        index_outer = 0
        while index_outer < len(nums1):
            outer_element = nums1[index_outer]
            dict_keys = list(mapping_freqs.keys())
            i_inner = 0
            while True:
                if i_inner >= len(dict_keys):
                    break
                key_inner = dict_keys[i_inner]
                val_inner_count = mapping_freqs[key_inner]
                test_dividend = outer_element
                test_divisor = key_inner * k
                if test_divisor != 0 and (test_dividend % test_divisor) == 0:
                    total_good_pairs += val_inner_count
                i_inner += 1
            index_outer += 1

        return total_good_pairs