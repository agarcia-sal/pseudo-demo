class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        q = 0
        u = len(initial)
        v = len(target)
        w = [[0] * (v + 1) for _ in range(u + 1)]
        x = 1
        while x <= u:
            y = 1
            while y <= v:
                if initial[x - 1] == target[y - 1]:
                    w[x][y] = w[x - 1][y - 1] + 1
                    if w[x][y] > q:
                        q = w[x][y]
                y += 1
            x += 1
        return u + v - 2 * q