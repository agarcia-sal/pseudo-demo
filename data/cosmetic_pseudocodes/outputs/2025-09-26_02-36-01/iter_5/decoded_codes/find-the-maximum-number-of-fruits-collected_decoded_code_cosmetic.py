class Solution:
    def maxCollectedFruits(self, fruits):
        size = len(fruits)

        directionsOne = [(1, 1), (1, 0)]
        directionsTwo = [(1, -1), (1, 0), (1, 1)]
        directionsThree = [(-1, 1), (0, 1), (1, 1)]

        cache = {}

        def dp(p1x, p1y, p2x, p2y, p3x, p3y):
            def outOfBounds(a, b):
                return a < 0 or a >= size or b < 0 or b >= size

            if outOfBounds(p1x, p1y) or outOfBounds(p2x, p2y) or outOfBounds(p3x, p3y):
                return -(1 << 28)

            if (p1x == p1y == p2x == p2y == p3x == p3y == size - 1):
                return fruits[size - 1][size - 1]

            key = (p1x, p1y, p2x, p2y, p3x, p3y)
            if key in cache:
                return cache[key]

            sum_collected = fruits[p1y][p1x]

            # If p1 coincides with p2 or p3, do not count p1's fruits
            if (p1x == p2x and p1y == p2y) or (p1x == p3x and p1y == p3y):
                sum_collected = 0

            # Add fruits from p2 and p3 position, avoiding double count if same
            if p2x == p3x and p2y == p3y:
                sum_collected += fruits[p2y][p2x]
            else:
                sum_collected += fruits[p2y][p2x] + fruits[p3y][p3x]

            max_next = -(1 << 28)

            for d1x, d1y in directionsOne:
                np1x, np1y = p1x + d1x, p1y + d1y
                for d2x, d2y in directionsTwo:
                    np2x, np2y = p2x + d2x, p2y + d2y
                    for d3x, d3y in directionsThree:
                        np3x, np3y = p3x + d3x, p3y + d3y
                        candidate = dp(np1x, np1y, np2x, np2y, np3x, np3y)
                        if candidate > max_next:
                            max_next = candidate

            result_val = sum_collected + max_next
            cache[key] = result_val
            return result_val

        startX1, startY1 = 0, 0
        startX2, startY2 = 0, size - 1
        startX3, startY3 = size - 1, 0

        output_val = dp(startX1, startY1, startX2, startY2, startX3, startY3)
        return output_val