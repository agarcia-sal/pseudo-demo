class Solution:
    def maxCollectedFruits(self, fruits):
        n = len(fruits)
        dir1 = [(1, 1), (0, 1)]
        dir2 = [(1, -1), (1, 0), (1, 1)]
        dir3 = [(-1, 1), (0, 1), (1, 1)]

        memo = {}

        def dp(x1, y1, x2, y2, x3, y3):
            if (x1 < 0 or x1 >= n or y1 < 0 or y1 >= n or
                x2 < 0 or x2 >= n or y2 < 0 or y2 >= n or
                x3 < 0 or x3 >= n or y3 < 0 or y3 >= n):
                return float('-inf')

            if (x1 == y1 == x2 == y2 == x3 == y3 == n - 1):
                return fruits[n - 1][n - 1]

            key = (x1, y1, x2, y2, x3, y3)
            if key in memo:
                return memo[key]

            collected = fruits[x1][y1]

            if (x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3):
                collected = 0

            if x2 == x3 and y2 == y3:
                collected += fruits[x2][y2]
            else:
                collected += fruits[x2][y2] + fruits[x3][y3]

            max_fruits = float('-inf')
            for dx1, dy1 in dir1:
                nx1, ny1 = x1 + dx1, y1 + dy1
                for dx2, dy2 in dir2:
                    nx2, ny2 = x2 + dx2, y2 + dy2
                    for dx3, dy3 in dir3:
                        nx3, ny3 = x3 + dx3, y3 + dy3
                        candidate = dp(nx1, ny1, nx2, ny2, nx3, ny3)
                        if candidate > max_fruits:
                            max_fruits = candidate

            memo[key] = collected + max_fruits
            return memo[key]

        return dp(0, 0, 0, n - 1, n - 1, 0)