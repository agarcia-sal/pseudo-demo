class Solution:
    def maxCollectedFruits(self, fruits):
        size = len(fruits)
        moves1 = [(1, 1), (0, 1)]
        moves2 = [(1, -1), (1, 0), (1, 1)]
        moves3 = [(-1, 1), (0, 1), (1, 1)]

        cache = {}

        def dp(x1, y1, x2, y2, x3, y3):
            if (
                x1 < 0 or x1 >= size or y1 < 0 or y1 >= size
                or x2 < 0 or x2 >= size or y2 < 0 or y2 >= size
                or x3 < 0 or x3 >= size or y3 < 0 or y3 >= size
            ):
                return float('-inf')

            if x1 == y1 == x2 == y2 == x3 == y3 == size - 1:
                return fruits[size - 1][size - 1]

            key = (x1, y1, x2, y2, x3, y3)
            if key in cache:
                return cache[key]

            total = fruits[x1][y1]

            if (x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3):
                total = 0

            if x2 == x3 and y2 == y3:
                total += fruits[x2][y2]
            else:
                total += fruits[x2][y2] + fruits[x3][y3]

            best = float('-inf')
            for dx1, dy1 in moves1:
                nx1, ny1 = x1 + dx1, y1 + dy1
                for dx2, dy2 in moves2:
                    nx2, ny2 = x2 + dx2, y2 + dy2
                    for dx3, dy3 in moves3:
                        nx3, ny3 = x3 + dx3, y3 + dy3
                        candidate = dp(nx1, ny1, nx2, ny2, nx3, ny3)
                        if candidate > best:
                            best = candidate

            cache[key] = total + best
            return total + best

        return dp(0, 0, 0, size - 1, size - 1, 0)