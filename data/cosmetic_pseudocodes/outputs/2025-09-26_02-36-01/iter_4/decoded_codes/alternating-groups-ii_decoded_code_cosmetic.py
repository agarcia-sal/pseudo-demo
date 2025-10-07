class Solution:
    def numberOfAlternatingGroups(self, colors: list, k: int) -> int:
        if k < 3:
            return 0

        total_elements = len(colors)
        wrapped_colors = colors + colors[:k - 1]

        valid_groups = 0
        idx = 0

        while idx < total_elements:
            alternating_flag = 1
            offset = 1

            while offset < k:
                pos_current = idx + offset
                pos_prev = pos_current - 1

                if wrapped_colors[pos_current] == wrapped_colors[pos_prev]:
                    alternating_flag = 0
                    break

                offset += 1

            if alternating_flag == 1:
                valid_groups += 1

            idx += 1

        return valid_groups