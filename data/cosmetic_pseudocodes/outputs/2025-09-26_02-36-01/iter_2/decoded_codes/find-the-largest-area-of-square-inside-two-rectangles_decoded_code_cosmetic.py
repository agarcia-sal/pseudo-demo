class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        def intersecting_square_area(bl1, tr1, bl2, tr2):
            left_bound = bl1[0] if bl1[0] > bl2[0] else bl2[0]
            right_bound = tr1[0] if tr1[0] < tr2[0] else tr2[0]
            bottom_bound = bl1[1] if bl1[1] > bl2[1] else bl2[1]
            top_bound = tr1[1] if tr1[1] < tr2[1] else tr2[1]

            if not (left_bound < right_bound and bottom_bound < top_bound):
                return 0

            width = right_bound - left_bound
            height = top_bound - bottom_bound
            edge_length = width if width < height else height

            return edge_length * edge_length

        maximum_area = 0
        total_squares = len(bottomLeft)
        current_index1 = 0

        while current_index1 < total_squares:
            current_index2 = current_index1 + 1
            while current_index2 < total_squares:
                area_candidate = intersecting_square_area(
                    bottomLeft[current_index1], topRight[current_index1],
                    bottomLeft[current_index2], topRight[current_index2]
                )
                if area_candidate > maximum_area:
                    maximum_area = area_candidate
                current_index2 += 1
            current_index1 += 1

        return maximum_area