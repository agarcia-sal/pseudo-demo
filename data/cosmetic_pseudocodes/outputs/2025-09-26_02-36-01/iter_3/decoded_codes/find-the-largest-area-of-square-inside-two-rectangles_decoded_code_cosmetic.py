class Solution:
    def largestSquareArea(self, blPoints, trPoints):
        def intersecting_square_area(blA, trA, blB, trB):
            x_left = blA[0]
            if blB[0] > x_left:
                x_left = blB[0]

            x_right = trA[0]
            if trB[0] < x_right:
                x_right = trB[0]

            y_bottom = blA[1]
            if blB[1] > y_bottom:
                y_bottom = blB[1]

            y_top = trA[1]
            if trB[1] < y_top:
                y_top = trB[1]

            if x_left >= x_right or y_bottom >= y_top:
                return 0

            width_x = x_right - x_left
            height_y = y_top - y_bottom

            edge_length = width_x if width_x < height_y else height_y

            return edge_length * edge_length

        length_points = len(blPoints)
        greatest_area = 0
        outer_index = 0
        while outer_index < length_points - 1:
            inner_index = outer_index + 1
            while inner_index < length_points:
                current_area = intersecting_square_area(
                    blPoints[outer_index], trPoints[outer_index],
                    blPoints[inner_index], trPoints[inner_index]
                )
                if current_area > greatest_area:
                    greatest_area = current_area
                inner_index += 1
            outer_index += 1

        return greatest_area