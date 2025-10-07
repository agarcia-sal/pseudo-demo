from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        if k < 3:
            return 0

        length = len(colors)
        extended_colors = [colors[i % length] for i in range(length + k - 1)]

        group_count = 0

        for start in range(length):
            for offset in range(1, k):
                if extended_colors[start + offset] == extended_colors[start + offset - 1]:
                    break
            else:
                group_count += 1

        return group_count