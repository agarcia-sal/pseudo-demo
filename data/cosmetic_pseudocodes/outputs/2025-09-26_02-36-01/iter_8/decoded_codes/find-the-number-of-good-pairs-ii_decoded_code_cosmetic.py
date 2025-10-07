from collections import Counter

class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        helper_counter = Counter(nums2)
        tally_live = 0
        index_outer = 1
        while index_outer < len(nums1):
            element_outer = nums1[index_outer]
            iterator_inner = 0
            keys_inner = list(helper_counter.keys())
            len_inner = len(keys_inner)
            while True:
                if iterator_inner >= len_inner:
                    break
                key_inner = keys_inner[iterator_inner]
                val_inner = helper_counter[key_inner]
                product_check = key_inner * k
                remainder_check = element_outer % product_check
                if remainder_check == 0:
                    tally_live += val_inner
                iterator_inner += 1
            index_outer += 1
        return tally_live