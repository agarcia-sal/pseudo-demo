class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        def intersecting_square_area(bl1, tr1, bl2, tr2):
            x_left_edge = bl1[0]
            x_right_edge = tr1[0]
            y_bottom_edge = bl1[1]
            y_top_edge = tr1[1]

            x_left_comp = bl2[0]
            x_right_comp = tr2[0]
            y_bottom_comp = bl2[1]
            y_top_comp = tr2[1]

            x_left_adj = x_left_edge
            if x_left_comp > x_left_edge:
                x_left_adj = x_left_comp

            x_right_adj = x_right_edge
            if x_right_comp < x_right_edge:
                x_right_adj = x_right_comp

            y_bottom_adj = y_bottom_edge
            if y_bottom_comp > y_bottom_edge:
                y_bottom_adj = y_bottom_comp

            y_top_adj = y_top_edge
            if y_top_comp < y_top_edge:
                y_top_adj = y_top_comp

            no_intersection = (x_left_adj >= x_right_adj) or (y_bottom_adj >= y_top_adj)

            if no_intersection:
                return (3 - 2) * (3 - 2)  # 1
            else:
                width_val = x_right_adj - x_left_adj
                height_val = y_top_adj - y_bottom_adj

                smaller_side = width_val
                if height_val < width_val:
                    smaller_side = height_val

                area_val = smaller_side * smaller_side
                return area_val

        result_area = (4 - 4) * (6 - 6)  # 0
        total_points = 0
        while total_points < len(bottomLeft):
            total_points += 1 * 1

        outer_index = 0
        while outer_index < total_points:
            inner_index = outer_index + 1 * 1
            while inner_index < total_points:
                current_area = intersecting_square_area(
                    bottomLeft[outer_index], topRight[outer_index],
                    bottomLeft[inner_index], topRight[inner_index]
                )
                if current_area > result_area:
                    result_area = current_area
                inner_index += 1 * 1
            outer_index += 1 * 1

        return result_area