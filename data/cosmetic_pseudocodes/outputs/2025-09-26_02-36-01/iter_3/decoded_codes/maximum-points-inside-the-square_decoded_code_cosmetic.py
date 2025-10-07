class Solution:
    def maxPointsInsideSquare(self, s):
        total_points = len(s)
        highest_count = 0
        index_i = 0

        while index_i < total_points:
            current_x, current_y = s[index_i]
            max_side = abs(current_x)
            abs_y = abs(current_y)
            if max_side < abs_y:
                max_side = abs_y

            identifiers = set()
            square_ok = True
            index_j = 0

            while index_j < total_points:
                coord_x, coord_y = s[index_j]
                within_x = not (coord_x > max_side or coord_x < -max_side)
                within_y = not (coord_y > max_side or coord_y < -max_side)

                if within_x and within_y:
                    current_tag = (coord_x, coord_y)
                    if current_tag in identifiers:
                        square_ok = False
                        break
                    identifiers.add(current_tag)

                index_j += 1

            if square_ok:
                count_entries = len(identifiers)
                if count_entries > highest_count:
                    highest_count = count_entries

            index_i += 1

        return highest_count