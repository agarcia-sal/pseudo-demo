from typing import List

class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        transformed_numbers = []
        for num in nums:
            remainder_list = []
            current_num = num
            while current_num > 0:
                remainder_list.insert(0, current_num % 2)
                current_num //= 2
            while len(remainder_list) < m:
                remainder_list.insert(0, 0)
            bin_form = ''.join(str(bit) for bit in remainder_list)
            transformed_numbers.append(bin_form)

        def hamming_distance(bin1: str, bin2: str) -> int:
            count_diff = 0
            for pos in range(len(bin1)):
                if bin1[pos] != bin2[pos]:
                    count_diff += 1
            return count_diff

        result_collection = []
        for outer_idx in range(len(nums)):
            max_found = 0
            for inner_idx in range(len(nums)):
                if outer_idx != inner_idx:
                    current_distance = hamming_distance(transformed_numbers[outer_idx], transformed_numbers[inner_idx])
                    if current_distance > max_found:
                        max_found = current_distance
            result_collection.append(max_found)

        return result_collection