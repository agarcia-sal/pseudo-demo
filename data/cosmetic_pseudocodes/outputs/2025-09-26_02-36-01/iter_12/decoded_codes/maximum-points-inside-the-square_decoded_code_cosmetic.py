class Solution:
    def maxPointsInsideSquare(self, s):
        def countDistinctTags(collection):
            tags_map = {}
            is_valid = True
            for idx in range(len(collection)):
                px, py = collection[idx][0], collection[idx][1]
                dist_bound = max(abs(collection[0][0]), abs(collection[0][1]))
                if abs(px) <= dist_bound and abs(py) <= dist_bound:
                    current_tag = s[idx]
                    if current_tag in tags_map:
                        is_valid = False
                        break
                    else:
                        tags_map[current_tag] = True
            return is_valid, len(tags_map)

        max_found = 0
        for iterator1 in range(len(s)):
            currentX, currentY = s[iterator1][0], s[iterator1][1]
            boundary = abs(currentX) if abs(currentX) > abs(currentY) else abs(currentY)

            filteredPoints = []
            for idx2 in range(len(s)):
                checkX, checkY = s[idx2][0], s[idx2][1]
                if abs(checkX) <= boundary and abs(checkY) <= boundary:
                    filteredPoints.append(s[idx2])

            valid, count = countDistinctTags(filteredPoints)
            if valid and count > max_found:
                max_found = count

        return max_found