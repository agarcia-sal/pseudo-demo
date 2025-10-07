from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        accumulator = 0
        iteration_var = 0
        n = len(possible)
        # Iterate over possible elements except the last one
        while iteration_var < n - 1:
            temp_val = (2 * possible[iteration_var]) - 1
            accumulator += temp_val
            iteration_var += 1

        contender_score = 0
        index_tracker = 0
        # Repeat while index_tracker <= len(possible) - 2
        while index_tracker <= n - 2:
            computed_val = (2 * possible[index_tracker]) - 1
            contender_score += computed_val
            accumulator -= computed_val
            if not (contender_score <= accumulator):
                return index_tracker + 1
            index_tracker += 1
        return -1