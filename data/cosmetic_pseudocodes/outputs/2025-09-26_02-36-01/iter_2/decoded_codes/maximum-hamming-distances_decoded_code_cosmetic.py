class Solution:
    def maxHammingDistances(self, nums: list[int], count: int) -> list[int]:
        bin_collection = []
        for val in nums:
            bin_rep = bin(val)[2:]  # convert to binary string without '0b'
            padding_needed = count - len(bin_rep)
            padded_bin = '0' * padding_needed + bin_rep
            bin_collection.append(padded_bin)

        def hamming_distance(binA: str, binB: str) -> int:
            diff_count = 0
            for charA, charB in zip(binA, binB):
                if charA != charB:
                    diff_count += 1
            return diff_count

        results = []
        for outer_idx in range(len(nums)):
            highest_dist = 0
            for inner_idx in range(len(nums)):
                if outer_idx != inner_idx:
                    current_dist = hamming_distance(bin_collection[outer_idx], bin_collection[inner_idx])
                    if highest_dist < current_dist:
                        highest_dist = current_dist
            results.append(highest_dist)
        return results