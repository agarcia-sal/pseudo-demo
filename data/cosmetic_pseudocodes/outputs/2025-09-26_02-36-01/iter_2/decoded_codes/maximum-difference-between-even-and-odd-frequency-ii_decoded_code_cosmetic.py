from collections import defaultdict
from math import inf

class Solution:
    def maxDifference(self, s: str, k: int) -> float:
        maximum_difference = -inf
        chars = ['0', '1', '2', '3', '4']
        pairs = [(chars[i], chars[j]) for i in range(len(chars)) for j in range(len(chars)) if i != j]

        for x, y in pairs:
            minimal_diff_map = defaultdict(lambda: inf)
            prefix_count_x = [0]
            prefix_count_y = [0]
            start_idx = 0
            index = 0
            length = len(s)

            while index < length:
                current_char = s[index]

                increment_x = 1 if current_char == x else 0
                increment_y = 1 if current_char == y else 0

                prefix_count_x.append(prefix_count_x[-1] + increment_x)
                prefix_count_y.append(prefix_count_y[-1] + increment_y)

                while (index - start_idx + 1) >= k and prefix_count_x[start_idx] < prefix_count_x[-1] and prefix_count_y[start_idx] < prefix_count_y[-1]:
                    parity_key = (prefix_count_x[start_idx] % 2, prefix_count_y[start_idx] % 2)
                    candidate_value = prefix_count_x[start_idx] - prefix_count_y[start_idx]
                    if candidate_value < minimal_diff_map[parity_key]:
                        minimal_diff_map[parity_key] = candidate_value
                    start_idx += 1

                current_parity_key = ((prefix_count_x[-1] - 1) % 2, prefix_count_y[-1] % 2)
                current_diff = prefix_count_x[-1] - prefix_count_y[-1] - minimal_diff_map[current_parity_key]
                if current_diff > maximum_difference:
                    maximum_difference = current_diff

                index += 1

        return maximum_difference