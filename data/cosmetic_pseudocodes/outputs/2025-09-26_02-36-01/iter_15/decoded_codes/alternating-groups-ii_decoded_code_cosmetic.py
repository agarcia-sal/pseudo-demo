class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        if k < 3:
            return 0

        a = len(colors)
        b = colors[:]  # copy of colors
        b.extend(colors[:k])

        e = 0
        f = 0
        while f < a:
            g = True
            h = 1
            while h < k:
                if b[f + h] == b[f + h - 1]:
                    g = False
                    break
                h += 1
            if g:
                e += 1
            f += 1

        return e