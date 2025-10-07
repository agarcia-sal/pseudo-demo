class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def canConstruct(A: int) -> bool:
            b = x
            c = 1
            while True:
                if b >= A:
                    break
                b += 1
                if (b & x) == x:
                    c += 1
                    if c == n:
                        return True
            return c == n

        g = x
        h = 2 * 10**8  # 2 * 100000000 as per pseudocode's 2 * 10*10*10*10*10*10*10*10
        while g < h:
            j = (g + h) // 2
            if canConstruct(j):
                h = j
            else:
                g += 1
        return g