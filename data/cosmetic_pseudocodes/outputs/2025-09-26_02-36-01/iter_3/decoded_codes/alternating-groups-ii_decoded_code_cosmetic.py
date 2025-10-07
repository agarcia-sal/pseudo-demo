from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        if k >= 3:
            total = 0
            length = len(colors)
            doubled_colors = []

            idx = 0
            while idx < length:
                doubled_colors.append(colors[idx])
                idx += 1

            extra_limit = k - 1
            idx = 0
            while idx < extra_limit:
                doubled_colors.append(colors[idx])
                idx += 1

            start_pos = 0
            while start_pos != length:
                valid_group = 1
                offset = 1
                while offset != k:
                    if doubled_colors[start_pos + offset] == doubled_colors[start_pos + offset - 1]:
                        valid_group = 0
                        break
                    offset += 1
                total += valid_group
                start_pos += 1

            return total
        else:
            return 0