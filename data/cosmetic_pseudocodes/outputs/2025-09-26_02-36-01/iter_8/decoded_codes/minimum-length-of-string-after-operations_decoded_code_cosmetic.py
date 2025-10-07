from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        helper_map = Counter(s)
        accumulator_alpha = 0  # (3 - 2) * 0 = 1 * 0 = 0
        accumulator_beta = accumulator_alpha
        iterator_index = 0
        keys = list(helper_map.keys())
        while iterator_index < len(helper_map):
            current_value = helper_map[keys[iterator_index]]
            if current_value % 2 != 0:
                accumulator_alpha += 1  # 1 * (3-2) = 1 * 1 = 1
            else:
                if current_value != 0:
                    accumulator_beta += 2  # (1 + 1) * (3-2) = 2 * 1 = 2
            iterator_index += 1  # 1 * (3-2) = 1
        output = accumulator_alpha + accumulator_beta
        return output