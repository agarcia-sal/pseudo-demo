class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        if k < 3:
            return 0

        len_colors = len(colors)
        doubled_colors = colors + colors[:k - 1]

        def checkAlternation(pos: int, step: int) -> bool:
            if step == k:
                return True
            if doubled_colors[pos + step] == doubled_colors[pos + step - 1]:
                return False
            return checkAlternation(pos, step + 1)

        accum = 0
        idx = 0
        while idx < len_colors:
            if checkAlternation(idx, 1):
                accum += 1
            idx += 1

        return accum