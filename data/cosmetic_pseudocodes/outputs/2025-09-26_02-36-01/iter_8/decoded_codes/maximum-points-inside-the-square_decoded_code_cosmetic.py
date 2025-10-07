class Solution:
    def maxPointsInsideSquare(self, s):
        total_points = len(s)
        greatest_number = 0
        index_i = 0
        while index_i < total_points - 1:
            point_x = s[index_i][0]
            point_y = s[index_i][1]
            maximum_side = abs(point_x) if abs(point_x) > abs(point_y) else abs(point_y)
            count_map = {}
            is_valid = True
            index_j = 0
            while index_j < total_points:
                current_x = s[index_j][0]
                current_y = s[index_j][1]
                if abs(current_x) <= maximum_side and abs(current_y) <= maximum_side:
                    current_tag = s[index_j]
                    if current_tag in count_map:
                        is_valid = False
                        break
                    else:
                        count_map[current_tag] = True
                index_j += 1
            if is_valid and len(count_map) > greatest_number:
                greatest_number = len(count_map)
            index_i += 1
        return greatest_number