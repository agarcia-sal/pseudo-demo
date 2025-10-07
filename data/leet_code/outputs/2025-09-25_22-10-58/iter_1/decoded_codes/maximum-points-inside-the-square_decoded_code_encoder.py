class Solution:
    def maxPointsInsideSquare(self, points: list[list[int]]) -> int:
        n = len(points)
        max_points = 0
        for i in range(n):
            x1, y1 = points[i]
            side_length = max(abs(x1), abs(y1))
            tag_count = {}
            valid_square = True
            for j in range(n):
                x2, y2 = points[j]
                if abs(x2) <= side_length and abs(y2) <= side_length:
                    tag = points[j]
                    # Use tuple of coordinates as tag key to enforce uniqueness
                    tag_key = tuple(tag)
                    if tag_key in tag_count:
                        valid_square = False
                        break
                    tag_count[tag_key] = True
            if valid_square:
                max_points = max(max_points, len(tag_count))
        return max_points