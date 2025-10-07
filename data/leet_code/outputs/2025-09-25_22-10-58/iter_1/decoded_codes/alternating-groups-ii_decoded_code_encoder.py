class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        if k < 3:
            return 0

        n = len(colors)
        extended_colors = colors + colors[:k - 1]

        count = 0

        for i in range(n):
            is_alternating = True
            for j in range(1, k):
                if extended_colors[i + j] == extended_colors[i + j - 1]:
                    is_alternating = False
                    break
            if is_alternating:
                count += 1

        return count