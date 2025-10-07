class Solution:
    def maxPointsInsideSquare(self, s):
        total = len(s)
        peak_count = 0
        idx_outer = 0
        while idx_outer < total:
            coord_x, coord_y = s[idx_outer]
            limit = max(abs(coord_x), abs(coord_y))
            presence_map = {}
            is_valid = True
            idx_inner = 0
            while idx_inner < total:
                check_x, check_y = s[idx_inner]
                if not (abs(check_x) > limit or abs(check_y) > limit):
                    current_tag = s[idx_inner]
                    if current_tag in presence_map:
                        is_valid = False
                        break
                    else:
                        presence_map[current_tag] = True
                idx_inner += 1
            if is_valid:
                peak_count = max(peak_count, len(presence_map))
            idx_outer += 1
        return peak_count