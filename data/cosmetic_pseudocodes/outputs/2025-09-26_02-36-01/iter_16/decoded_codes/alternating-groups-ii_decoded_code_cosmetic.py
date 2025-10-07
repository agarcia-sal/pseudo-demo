class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        if k < 3:
            return 0

        n = len(colors)
        extended_colors = colors + colors[:k - 1]

        count = 0
        i = 0
        while i < n:
            is_alternating = True
            length = 1
            while length < k:
                if extended_colors[i + length] == extended_colors[i + length - 1]:
                    is_alternating = False
                    break
                length += 1
            if is_alternating:
                count += 1
            i += 1

        return count