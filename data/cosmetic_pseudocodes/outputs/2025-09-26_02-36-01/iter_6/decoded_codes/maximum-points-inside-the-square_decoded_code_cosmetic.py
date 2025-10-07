class Solution:
    def maxPointsInsideSquare(self, s):
        def absoluteValue(num):
            return -num if num < 0 else num

        total_points = len(s)
        highest_count = 0
        idx_primary = 0

        while idx_primary < total_points:
            coordinate_x, coordinate_y = s[idx_primary]

            magnitude_x = absoluteValue(coordinate_x)
            magnitude_y = absoluteValue(coordinate_y)

            max_side = magnitude_y if magnitude_x < magnitude_y else magnitude_x

            observed_tags = {}
            can_accept = True

            def PROCESS_SECONDARY(current):
                nonlocal can_accept
                if current >= total_points:
                    return

                candidate_x, candidate_y = s[current]

                abs_candidate_x = absoluteValue(candidate_x)
                abs_candidate_y = absoluteValue(candidate_y)

                if abs_candidate_x <= max_side and abs_candidate_y <= max_side:
                    tag_identifier = s[current]
                    if tag_identifier in observed_tags:
                        can_accept = False
                        return
                    else:
                        observed_tags[tag_identifier] = True

                PROCESS_SECONDARY(current + 1)

            PROCESS_SECONDARY(0)

            if can_accept:
                count = len(observed_tags)
                if count > highest_count:
                    highest_count = count

            idx_primary += 1

        return highest_count