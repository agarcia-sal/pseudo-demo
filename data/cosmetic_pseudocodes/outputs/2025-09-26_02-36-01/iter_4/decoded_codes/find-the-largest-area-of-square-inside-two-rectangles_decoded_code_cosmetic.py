class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        def intersecting_square_area(bl1, tr1, bl2, tr2):
            # Determine the left edge of the overlapping rectangle
            left_edge = bl2[0] if bl1[0] < bl2[0] else bl1[0]
            # Determine the right edge of the overlapping rectangle
            right_edge = tr1[0] if tr1[0] <= tr2[0] else tr2[0]
            # Determine the bottom edge of the overlapping rectangle
            bottom_edge = bl1[1] if bl1[1] <= bl2[1] else bl2[1]
            # Determine the top edge of the overlapping rectangle
            top_edge = tr1[1] if tr1[1] < tr2[1] else tr2[1]

            if left_edge >= right_edge or bottom_edge >= top_edge:
                return 0
            width = right_edge - left_edge
            height = top_edge - bottom_edge
            side_length = width if width < height else height
            return side_length * side_length

        maximum_area_value = 0
        total_points = len(bottomLeft)
        outer_index = 0
        while outer_index < total_points - 1:
            inner_index = outer_index + 1
            while inner_index < total_points:
                first_bl = bottomLeft[outer_index]
                first_tr = topRight[outer_index]
                second_bl = bottomLeft[inner_index]
                second_tr = topRight[inner_index]
                current_area = intersecting_square_area(first_bl, first_tr, second_bl, second_tr)
                if maximum_area_value < current_area:
                    maximum_area_value = current_area
                inner_index += 1
            outer_index += 1
        return maximum_area_value