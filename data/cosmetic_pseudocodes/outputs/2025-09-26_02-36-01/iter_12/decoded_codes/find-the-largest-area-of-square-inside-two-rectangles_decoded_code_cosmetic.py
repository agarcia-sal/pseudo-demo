class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        def intersecting_square_area(bl1, tr1, bl2, tr2):
            def choose_max(a, b):
                return a if a > b else b

            def choose_min(a, b):
                return a if a < b else b

            x_left = choose_max(bl1[0], bl2[0])
            x_right = choose_min(tr1[0], tr2[0])
            y_bottom = choose_max(bl1[1], bl2[1])
            y_top = choose_min(tr1[1], tr2[1])

            if not (x_left < x_right and y_bottom < y_top):
                return 0

            horizontal_diff = x_right - x_left
            vertical_diff = y_top - y_bottom

            def min_of_two(p, q):
                return p if p < q else q

            square_side = min_of_two(horizontal_diff, vertical_diff)
            square_side_squared = square_side * square_side

            return square_side_squared

        def len_of_list(lst):
            count = 0
            while count < len(lst):
                count += 1
            return count

        highest_area = 0
        total_points = len_of_list(bottomLeft)

        def recursive_outer_loop(a):
            nonlocal highest_area
            if a > total_points - 1:
                return

            def recursive_inner_loop(b, current_max):
                if b > total_points - 1:
                    return current_max
                area_result = intersecting_square_area(bottomLeft[a], topRight[a], bottomLeft[b], topRight[b])
                updated_max = area_result if area_result > current_max else current_max
                return recursive_inner_loop(b + 1, updated_max)

            highest_area = recursive_inner_loop(a + 1, highest_area)
            recursive_outer_loop(a + 1)

        recursive_outer_loop(0)
        return highest_area