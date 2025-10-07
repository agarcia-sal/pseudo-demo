class Solution:
    def maxHammingDistances(self, nums: list[int], m: int) -> list[int]:
        def compute_hamming_distance(a: str, b: str) -> int:
            def recursive_compare(idx: int, acc: int) -> int:
                if idx == len(a):
                    return acc
                increment = 1 if a[idx] != b[idx] else 0
                return recursive_compare(idx + 1, acc + increment)
            return recursive_compare(0, 0)

        def build_binary_list(src: list[int], count: int) -> list[str]:
            def helper(pos: int, acc_list: list[str]) -> list[str]:
                if pos == count:
                    return acc_list

                temp_num = src[pos]

                def convert_to_bin(value: int, bits_left: int, acc_str: str) -> str:
                    if bits_left == 0:
                        return acc_str
                    bit_char = '1' if (value % 2) == 1 else '0'
                    return convert_to_bin(value // 2, bits_left - 1, bit_char + acc_str)

                formatted_bin = convert_to_bin(temp_num, m, "")
                return helper(pos + 1, acc_list + [formatted_bin])

            return helper(0, [])

        accumulated_bin_repr = build_binary_list(nums, len(nums))

        def find_max_for_index(current_index: int, total_len: int) -> int:
            def inner_loop(compare_index: int, current_max: int) -> int:
                if compare_index == total_len:
                    return current_max

                dist_val = 0
                if current_index != compare_index:
                    dist_val = compute_hamming_distance(accumulated_bin_repr[current_index], accumulated_bin_repr[compare_index])

                next_max = current_max
                if dist_val > current_max:
                    next_max = dist_val

                return inner_loop(compare_index + 1, next_max)

            return inner_loop(0, 0)

        def gather_results(pos: int, total_len: int, result_acc: list[int]) -> list[int]:
            if pos == total_len:
                return result_acc
            max_distance_val = find_max_for_index(pos, total_len)
            return gather_results(pos + 1, total_len, result_acc + [max_distance_val])

        return gather_results(0, len(nums), [])