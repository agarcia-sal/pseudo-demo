class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        tally_map = {}
        for zeta in range(len(nums2)):
            val = nums2[zeta]
            tally_map[val] = tally_map.get(val, 0) + 1

        accumulator = 0
        iterator_alpha = 0
        while iterator_alpha < len(nums1):
            current_num1 = nums1[iterator_alpha]
            for key_beta, val_gamma in tally_map.items():
                if (current_num1 % (key_beta * k)) == 0:
                    accumulator += val_gamma
            iterator_alpha += 1

        return accumulator