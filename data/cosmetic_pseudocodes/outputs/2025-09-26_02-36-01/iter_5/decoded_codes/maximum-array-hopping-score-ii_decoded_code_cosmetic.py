from typing import List

class Solution:
    def maxScore(self, vals: List[int]) -> int:
        length_var = len(vals)
        results = [0] * length_var

        def traverse(index: int) -> int:
            if index == length_var:
                return 0
            else:
                def inner_loop(pos: int, current_max: int) -> int:
                    if pos == length_var:
                        return current_max
                    else:
                        distance = pos - index
                        temp_score = distance * vals[pos]
                        candidate = temp_score + results[pos]
                        if current_max < candidate:
                            current_max = candidate
                        return inner_loop(pos + 1, current_max)

                accumulator = inner_loop(index + 1, 0)
                results[index] = accumulator
                return traverse(index + 1)

        traverse(0)
        final_result = results[0]
        return final_result