class Solution:
    def maxPointsInsideSquare(self, s):
        total_points = len(s)
        highest_points = 0
        idx_outer = 0
        while idx_outer < total_points:
            coordinate_a = s[idx_outer][0]
            coordinate_b = s[idx_outer][1]

            abs_a = coordinate_a if coordinate_a >= 0 else -coordinate_a
            abs_b = coordinate_b if coordinate_b >= 0 else -coordinate_b
            length_side = abs_a if abs_a > abs_b else abs_b

            markers_seen = {}
            is_square_valid = True
            idx_inner = 0
            while idx_inner < total_points and is_square_valid:
                curr_x = s[idx_inner][0]
                curr_y = s[idx_inner][1]
                if not (curr_x > length_side or curr_x < -length_side or curr_y > length_side or curr_y < -length_side):
                    current_tag = s[idx_inner]
                    if current_tag in markers_seen:
                        is_square_valid = False
                    else:
                        markers_seen[current_tag] = True
                idx_inner += 1

            if is_square_valid:
                if len(markers_seen) > highest_points:
                    highest_points = len(markers_seen)

            idx_outer += 1

        return highest_points