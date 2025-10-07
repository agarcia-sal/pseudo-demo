class Solution:
    def maxPointsInsideSquare(self, s):
        total_points = len(s)
        highest_count = 0
        index_i = 0
        while index_i < total_points:
            coordinate_x = s[index_i][0]
            coordinate_y = s[index_i][1]

            absolute_x = coordinate_x if coordinate_x >= 0 else -coordinate_x
            absolute_y = coordinate_y if coordinate_y >= 0 else -coordinate_y

            square_edge = absolute_x if absolute_x >= absolute_y else absolute_y

            observed_tags = {}
            is_valid_square = True

            index_j = 0
            while index_j < total_points:
                point_x = s[index_j][0]
                point_y = s[index_j][1]

                abs_x_check = point_x if point_x >= 0 else -point_x
                abs_y_check = point_y if point_y >= 0 else -point_y

                if abs_x_check <= square_edge and abs_y_check <= square_edge:
                    current_tag = s[index_j]
                    if current_tag in observed_tags:
                        is_valid_square = False
                        break
                    else:
                        observed_tags[current_tag] = True
                index_j += 1

            if is_valid_square:
                count_tags = len(observed_tags)
                if count_tags > highest_count:
                    highest_count = count_tags

            index_i += 1

        return highest_count