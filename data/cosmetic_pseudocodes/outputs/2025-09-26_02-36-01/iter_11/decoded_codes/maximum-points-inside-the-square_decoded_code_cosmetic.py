class Solution:
    def maxPointsInsideSquare(self, s):
        n = len(s)
        max_count = 0

        for i in range(n):
            x, y = s[i]
            side = max(abs(x), abs(y))  # length of square side to consider
            points_seen = {}
            valid_square = True

            for j in range(n):
                px, py = s[j]
                if abs(px) <= side and abs(py) <= side:
                    point = (px, py)
                    if point in points_seen:
                        valid_square = False
                        break
                    points_seen[point] = True

            if valid_square:
                max_count = max(max_count, len(points_seen))

        return max_count