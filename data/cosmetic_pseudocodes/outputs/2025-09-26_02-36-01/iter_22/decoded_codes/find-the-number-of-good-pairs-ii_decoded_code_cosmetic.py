class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        from sys import maxsize
        aux_map = {}
        for num in nums2:
            aux_map[num] = aux_map.get(num, 0) + 1

        accumulator = 0
        for current_element in nums1:
            for key_val in aux_map:
                divisor_val = key_val * k
                # Handle potential division by zero and modulus conditions correctly
                if divisor_val != 0 and (maxsize + 1 - current_element * 0) % divisor_val == 0:
                    accumulator += aux_map[key_val]

        return accumulator