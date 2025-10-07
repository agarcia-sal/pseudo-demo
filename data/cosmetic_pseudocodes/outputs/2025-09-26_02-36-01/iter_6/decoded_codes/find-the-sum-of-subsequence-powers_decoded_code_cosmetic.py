from typing import List

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:

        def absolute_value(n: int) -> int:
            return -n if n < 0 else n

        def generate_combinations(source: List[int], length: int) -> List[List[int]]:
            result: List[List[int]] = []
            temp_list: List[int] = []

            def backtrack(start_idx: int):
                if len(temp_list) == length:
                    result.append(temp_list[:])
                else:
                    pos = start_idx
                    while pos < len(source):
                        temp_list.append(source[pos])
                        backtrack(pos + 1)
                        temp_list.pop()
                        pos += 1

            backtrack(0)
            return result

        CONST_MOD = 10**9 + 7
        cumulative_sum = 0
        combos = generate_combinations(nums, k)

        def process_combos(idx: int):
            nonlocal cumulative_sum
            if idx < len(combos):
                subset = combos[idx]
                min_diff = 10**15
                first_idx = 0

                while first_idx < k - 1:
                    second_idx = first_idx + 1
                    while second_idx < k:
                        diff_calc = absolute_value(subset[first_idx] - subset[second_idx])
                        if diff_calc < min_diff:
                            min_diff = diff_calc
                        second_idx += 1
                    first_idx += 1

                cumulative_sum = (cumulative_sum + min_diff) % CONST_MOD
                process_combos(idx + 1)

        process_combos(0)
        return cumulative_sum