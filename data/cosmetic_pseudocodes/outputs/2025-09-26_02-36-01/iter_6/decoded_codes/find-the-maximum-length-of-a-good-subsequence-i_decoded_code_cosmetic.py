class Solution:
    def maximumLength(self, a: list, b: int) -> int:
        c = len(a)
        d = [[1] * (b + 1) for _ in range(c)]
        e = 0

        p = 0
        while p < c:
            q = 0
            while q <= b:
                r = p - 1
                while r >= 0:
                    if a[p] == a[r]:
                        if d[p][q] < d[r][q] + 1:
                            d[p][q] = d[r][q] + 1
                    else:
                        if q > 0:
                            if d[p][q] < d[r][q - 1] + 1:
                                d[p][q] = d[r][q - 1] + 1
                    r -= 1
                q += 1
            if e < d[p][b]:
                e = d[p][b]
            p += 1

        return e