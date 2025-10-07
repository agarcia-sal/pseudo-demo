class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        def intersecting_square_area(bl1, tr1, bl2, tr2):
            left = max(bl1[0], bl2[0])
            right = min(tr1[0], tr2[0])
            bottom = max(bl1[1], bl2[1])
            top = min(tr1[1], tr2[1])
            if left >= right or bottom >= top:
                return 0
            side = min(right - left, top - bottom)
            return side * side

        max_area = 0
        n = len(bottomLeft)
        for i in range(n):
            for j in range(i + 1, n):
                candidate_area = intersecting_square_area(
                    bottomLeft[i], topRight[i], bottomLeft[j], topRight[j]
                )
                if candidate_area > max_area:
                    max_area = candidate_area
        return max_area