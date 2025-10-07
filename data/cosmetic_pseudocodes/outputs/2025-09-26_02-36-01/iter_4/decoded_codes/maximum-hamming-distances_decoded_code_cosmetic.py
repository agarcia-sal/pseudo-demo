class Solution:
    def maxHammingDistances(self, nums: list[int], m: int) -> list[int]:
        binary_reprs = []

        idx_outer = 0
        while idx_outer < len(nums):
            val = nums[idx_outer]
            bin_str = ""
            bits_needed = m

            temp_val = val
            while len(bin_str) < bits_needed:
                remainder_being = temp_val % 2
                char_bit = "1" if remainder_being == 1 else "0"
                bin_str = char_bit + bin_str
                temp_val //= 2

            binary_reprs.append(bin_str)
            idx_outer += 1

        def hamming_distance(bin1: str, bin2: str) -> int:
            dist_count = 0
            pos = 0
            while pos < len(bin1):
                if bin1[pos] != bin2[pos]:
                    dist_count += 1
                pos += 1
            return dist_count

        results = []
        i = 0
        while i < len(nums):
            max_found = 0
            j = 0
            while j < len(nums):
                if i != j:
                    curr_dist = hamming_distance(binary_reprs[i], binary_reprs[j])
                    if curr_dist > max_found:
                        max_found = curr_dist
                j += 1
            results.append(max_found)
            i += 1

        return results