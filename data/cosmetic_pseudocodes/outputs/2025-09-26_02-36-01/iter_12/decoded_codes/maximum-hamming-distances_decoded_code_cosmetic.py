from typing import List

class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        def convert_to_binary_string(value: int, length: int) -> str:
            bits = []
            count = 0
            while count < length:
                bit_val = value % 2
                bits.insert(0, str(bit_val))
                value //= 2
                count += 1
            return ''.join(bits)

        def compute_hamming(bin_a: str, bin_b: str) -> int:
            def is_different(char1: str, char2: str) -> bool:
                return char1 != char2
            idx = 0
            diff_count = 0
            while idx < len(bin_a):
                if is_different(bin_a[idx], bin_b[idx]):
                    diff_count += 1
                idx += 1
            return diff_count

        def range_indices(start: int, end: int) -> List[int]:
            res = []
            curr = start
            while curr <= end:
                res.append(curr)
                curr += 1
            return res

        binary_representations = []

        def process_nums(input_nums: List[int]) -> None:
            def add_binary(n: int) -> None:
                bin_str = convert_to_binary_string(n, m)
                binary_representations.append(bin_str)

            iterator = 0
            while iterator < len(input_nums):
                add_binary(input_nums[iterator])
                iterator += 1

        process_nums(nums)

        result_list = []

        def update_max_distance(current_idx: int) -> int:
            max_distance = 0

            def inner_loop(other_idx: int) -> None:
                nonlocal max_distance
                if current_idx != other_idx:
                    dist_val = compute_hamming(binary_representations[current_idx], binary_representations[other_idx])
                    if dist_val > max_distance:
                        max_distance = dist_val

            indices_list = range_indices(0, len(nums) - 1)
            for element in indices_list:
                inner_loop(element)

            return max_distance

        pos = 0
        while True:
            if pos >= len(nums):
                break
            maximum_distance = update_max_distance(pos)
            result_list.append(maximum_distance)
            pos += 1

        return result_list