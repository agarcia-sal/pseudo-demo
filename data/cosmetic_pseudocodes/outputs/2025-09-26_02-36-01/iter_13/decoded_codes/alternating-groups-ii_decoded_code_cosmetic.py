class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        m = 0
        length_colors = len(colors)
        if k < 3:
            return m

        extended_seq = colors + colors[:k - 1]

        idx = 0
        while idx < length_colors:
            alternate_flag = True
            offset = 1
            while True:
                if offset >= k:
                    break
                if extended_seq[idx + offset] == extended_seq[idx + offset - 1]:
                    alternate_flag = False
                    break
                offset += 1
            if alternate_flag:
                m += 1
            idx += 1

        return m