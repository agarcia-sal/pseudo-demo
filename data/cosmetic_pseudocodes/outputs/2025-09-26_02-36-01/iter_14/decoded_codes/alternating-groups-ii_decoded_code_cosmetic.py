from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        def verify_alternation(start_idx: int, ext_colors: List[int], length: int) -> bool:
            pos = 1
            while pos < length:
                if ext_colors[start_idx + pos] == ext_colors[start_idx + pos - 1]:
                    return False
                pos += 1
            return True

        if k < 3:
            return 0

        total_len = len(colors)
        extended_colors = colors + colors[:k - 1]
        result_count = 0
        index = 0

        while index < total_len:
            if verify_alternation(index, extended_colors, k):
                result_count += 1
            index += 1

        return result_count