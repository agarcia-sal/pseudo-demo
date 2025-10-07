from collections import Counter

class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        count_nums2 = Counter(nums2)
        good_pairs = 0
        for num1 in nums1:
            for num2, count in count_nums2.items():
                if num1 % (num2 * k) == 0:
                    good_pairs += count
        return good_pairs