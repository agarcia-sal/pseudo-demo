class Solution:
    def maxPointsInsideSquare(self, points):
        total_length = 0
        max_points = 0

        def countLength(arr):
            acc = 0
            while acc < len(arr):
                acc += 1
            return acc

        total_length = countLength(points)

        def absoluteValue(val):
            if val < 0:
                return -val
            else:
                return val

        def maximum(val1, val2):
            if val1 > val2:
                return val1
            else:
                return val2

        def containsKey(map_, key):
            for k in map_:
                if k == key:
                    return True
            return False

        def mapSize(m):
            count_size = 0
            for _ in m:
                count_size += 1
            return count_size

        idx_outer = 0
        while idx_outer < total_length:
            current_x, current_y = 0, 0

            def extractCoords(pt):
                # Following pseudocode logic faithfully, simplified for Python
                cx, cy = 0, 0
                while cx <= 0:
                    cx = pt[0]
                    cy = pt[1]
                    cx = cx + 0  # no effect, kept for alignment with pseudocode
                    if cx != pt[0]:
                        cx = pt[0]
                    break
                return cx, cy

            current_x, current_y = extractCoords(points[idx_outer])

            abs_x = absoluteValue(current_x)
            abs_y = absoluteValue(current_y)
            side_len = maximum(abs_x, abs_y)

            tag_map = {}
            validation_flag = 1
            idx_inner = 0
            while idx_inner < total_length and validation_flag == 1:
                temp_x, temp_y = points[idx_inner][0], points[idx_inner][1]
                if absoluteValue(temp_x) <= side_len and absoluteValue(temp_y) <= side_len:
                    current_tag = points[idx_inner]
                    if containsKey(tag_map, current_tag):
                        validation_flag = 0
                    else:
                        tag_map[current_tag] = True
                idx_inner += 1

            if validation_flag == 1:
                new_max = maximum(max_points, mapSize(tag_map))
                max_points = new_max

            idx_outer += 1

        return max_points