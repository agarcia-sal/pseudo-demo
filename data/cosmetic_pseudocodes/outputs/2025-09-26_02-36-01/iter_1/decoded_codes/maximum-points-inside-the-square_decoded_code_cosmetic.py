class Solution:
    def maxPointsInsideSquare(self, s):
        total_points = len(s)
        maximum_covered = 0
        for index in range(total_points):
            current_x, current_y = s[index]
            boundary = max(abs(current_x), abs(current_y))
            encountered_tags = {}
            is_square_valid = True
            for idx in range(total_points):
                candidate_x, candidate_y = s[idx]
                if abs(candidate_x) <= boundary and abs(candidate_y) <= boundary:
                    candidate_tag = s[idx]
                    if candidate_tag in encountered_tags:
                        is_square_valid = False
                        break
                    else:
                        encountered_tags[candidate_tag] = True
            if is_square_valid:
                current_count = len(encountered_tags)
                if current_count > maximum_covered:
                    maximum_covered = current_count
        return maximum_covered