class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        frequency_map = {}
        for element in nums2:
            frequency_map[element] = frequency_map.get(element, 0) + 1

        total_pairs = 0
        for current_value in nums1:
            for key, count in frequency_map.items():
                divisor = key * k
                if divisor != 0 and current_value % divisor == 0:
                    total_pairs += count

        return total_pairs