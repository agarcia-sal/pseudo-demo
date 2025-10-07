class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        w = len(caption)
        if w < 3:
            return ""
        x = list(caption)
        u = 0
        while u < w:
            p = u
            q = p
            while q < w and x[q] == x[p]:
                q += 1
            r = q - p
            if r < 3:
                if p > 0 and x[p - 1] == x[p]:
                    x[p - 1] = x[p]
                    p -= 1
                    r += 1
                if q < w and x[q - 1] == x[q]:
                    x[q] = x[q - 1]
                    q += 1
                    r += 1
                if r < 3:
                    v = x[p - 1] if p > 0 else x[q]
                    if v == 'a':
                        v = 'b'
                    elif v == 'z':
                        v = 'y'
                    else:
                        v = chr(ord(v) + 1)
                    for s in range(r):
                        x[p + s] = v
                    u = p + r
                    continue
            u = q
        return "".join(x)