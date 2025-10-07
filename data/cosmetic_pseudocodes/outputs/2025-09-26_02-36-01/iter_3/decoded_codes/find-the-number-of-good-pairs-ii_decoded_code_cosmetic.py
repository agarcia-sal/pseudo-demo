class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        freq_map = {}
        for val in nums2:
            freq_map[val] = freq_map.get(val, 0) + 1

        total_pairs = 0
        for current_val in nums1:
            for keyVal, times in freq_map.items():
                product_val = keyVal * k
                if product_val != 0 and current_val % product_val == 0:
                    total_pairs += times
        return total_pairs