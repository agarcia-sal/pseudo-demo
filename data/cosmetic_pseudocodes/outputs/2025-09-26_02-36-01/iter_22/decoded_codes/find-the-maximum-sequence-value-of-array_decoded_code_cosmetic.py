class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        p = 1
        q = 0
        while q < 7:
            p *= 2
            q += 1

        r = 0
        s = len(nums)

        def Initialize3DBooleanArray(d1, d2, d3):
            # Creates a 3D list of booleans initialized to False
            return [[[False] * d3 for _ in range(d2)] for __ in range(d1)]

        f = Initialize3DBooleanArray(s + 1, k + 2, p)
        f[0][0][0] = True

        i = 0
        while i < s:
            j = 0
            while j <= k:
                x = 0
                while x < p:
                    index1 = i + 1
                    val1 = f[index1][j][x] or f[i][j][x]
                    f[index1][j][x] = val1

                    index2 = j + 1
                    newX = x | nums[i]
                    val2 = f[index1][index2][newX] or f[i][j][x]
                    f[index1][index2][newX] = val2
                    x += 1
                j += 1
            i += 1

        g = Initialize3DBooleanArray(s + 1, k + 2, p)
        g[s][0][0] = True

        u = s
        while u > 0:
            v = 0
            while v <= k:
                w = 0
                while w < p:
                    idx1 = u - 1
                    val3 = g[idx1][v][w] or g[u][v][w]
                    g[idx1][v][w] = val3

                    idx2 = v + 1
                    newVal = w | nums[u - 1]
                    val4 = g[idx1][idx2][newVal] or g[u][v][w]
                    g[idx1][idx2][newVal] = val4
                    w += 1
                v += 1
            u -= 1

        answer = 0
        outer = k
        while outer <= s - k:
            midX = 0
            while midX < p:
                if f[outer][k][midX]:
                    innerY = 0
                    while innerY < p:
                        if g[outer][k][innerY]:
                            candidate = midX ^ innerY
                            if candidate > answer:
                                answer = candidate
                        innerY += 1
                midX += 1
            outer += 1

        return answer