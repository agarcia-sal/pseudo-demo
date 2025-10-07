class Solution:
    def maxPointsInsideSquare(self, s):
        total_entries = len(s)
        maximum_marked = 0
        outer_index = 0
        while outer_index < total_entries:
            coord_x, coord_y = s[outer_index]
            boundary_limit = abs(coord_x) if abs(coord_x) >= abs(coord_y) else abs(coord_y)
            encountered_tags = {}
            is_square_valid = True
            inner_index = 0
            while True:
                if inner_index >= total_entries:
                    break
                curr_x, curr_y = s[inner_index]
                if abs(curr_x) <= boundary_limit and abs(curr_y) <= boundary_limit:
                    current_tag = s[inner_index]
                    if current_tag in encountered_tags:
                        is_square_valid = not is_square_valid
                        break
                    else:
                        encountered_tags[current_tag] = True
                inner_index += 1
            if is_square_valid:
                maximum_marked = maximum_marked if maximum_marked >= len(encountered_tags) else len(encountered_tags)
            outer_index += 1
        return maximum_marked