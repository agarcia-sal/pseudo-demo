from collections import Counter

class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        freq_map = Counter(nums2)
        total_pairs = 0
        for element1 in nums1:
            for key, occurrences in freq_map.items():
                if key * k != 0 and element1 % (key * k) == 0:
                    total_pairs += occurrences
        return total_pairs