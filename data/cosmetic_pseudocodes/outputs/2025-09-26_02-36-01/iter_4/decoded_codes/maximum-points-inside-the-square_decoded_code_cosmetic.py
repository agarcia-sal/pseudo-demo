class Solution:
    def maxPointsInsideSquare(self, s):
        total_points = len(s)
        greatest_points_found = 0

        i_index = 0
        while i_index < total_points:
            x_coord = s[i_index][0]
            y_coord = s[i_index][1]

            abs_x = x_coord if x_coord >= 0 else -x_coord
            abs_y = y_coord if y_coord >= 0 else -y_coord

            side_limit = abs_x
            if abs_y > side_limit:
                side_limit = abs_y

            encountered_tags = {}
            is_square_valid = True

            j_index = 0
            while j_index < total_points:
                current_x = s[j_index][0]
                current_y = s[j_index][1]

                abs_current_x = current_x if current_x >= 0 else -current_x
                abs_current_y = current_y if current_y >= 0 else -current_y

                if not (abs_current_x > side_limit or abs_current_y > side_limit):
                    curr_tag = s[j_index]
                    if curr_tag in encountered_tags:
                        is_square_valid = False
                        break
                    else:
                        encountered_tags[curr_tag] = True
                j_index += 1

            if is_square_valid:
                count_tags = len(encountered_tags)
                if count_tags > greatest_points_found:
                    greatest_points_found = count_tags

            i_index += 1

        return greatest_points_found