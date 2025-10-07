from itertools import combinations

class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        constant_mod = 10**9 + 7
        accumulator = 0
        combos = list(combinations(nums, k))

        outer_index = 0
        while outer_index < len(combos):
            current_combo = combos[outer_index]
            smallest_diff = 9999999999999

            i = 0
            while i < k - 1:
                j = i + 1
                while j < k:
                    diff = current_combo[j] - current_combo[i]
                    if diff < 0:
                        diff = -diff
                    if diff < smallest_diff:
                        smallest_diff = diff
                    j += 1
                i += 1

            accumulator = (accumulator + smallest_diff) % constant_mod
            outer_index += 1

        return accumulator