class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        result = 0
        if k < 3:
            return 0
        m = len(colors)
        expanded_colors = colors + colors[:k - 1]

        pos = 0
        while pos < m:
            valid = True
            offset = 1
            while offset < k:
                if expanded_colors[pos + offset - 1] == expanded_colors[pos + offset]:
                    valid = False
                    break
                offset += 1
            if valid:
                result += 1
            pos += 1
        return result