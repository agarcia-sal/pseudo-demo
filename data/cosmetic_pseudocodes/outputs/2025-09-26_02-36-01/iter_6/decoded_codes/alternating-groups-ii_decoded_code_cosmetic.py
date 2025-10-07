from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        if not (k >= 3):
            return 0

        length_colors = len(colors)
        extended_colors = colors + colors[:k - 1]

        total_alternating = 0

        def are_alternating_segment(start_idx: int, length_k: int) -> bool:
            def check_step(step: int) -> bool:
                if step == length_k:
                    return True
                val_current = extended_colors[start_idx + step]
                val_prev = extended_colors[start_idx + step - 1]
                if val_current != val_prev:
                    return check_step(step + 1)
                else:
                    return False
            return check_step(1)

        def iterate_forward(index: int) -> int:
            nonlocal total_alternating
            if index > length_colors - 1:
                return total_alternating
            if are_alternating_segment(index, k):
                total_alternating += 1
            return iterate_forward(index + 1)

        return iterate_forward(0)