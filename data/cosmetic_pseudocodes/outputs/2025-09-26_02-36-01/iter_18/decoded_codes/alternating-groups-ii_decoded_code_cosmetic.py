from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        if k < 3:
            return 0

        n = len(colors)
        extended_colors = colors + colors[:k-1]
        count = 0

        for i in range(n):
            valid = True
            for j in range(1, k):
                if extended_colors[i + j] == extended_colors[i + j - 1]:
                    valid = False
                    break
            if valid:
                count += 1
        return count