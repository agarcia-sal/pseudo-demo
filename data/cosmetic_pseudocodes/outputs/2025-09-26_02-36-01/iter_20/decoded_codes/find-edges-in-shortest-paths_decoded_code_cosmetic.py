from collections import defaultdict

class Solution:
    def findAnswer(self, n, edges):
        def createGraphMap():
            return defaultdict(list)

        def pushHeap(h, val):
            h.append(val)
            i = len(h) - 1
            while i > 0:
                parent = (i - 1) // 2
                if h[parent][0] <= h[i][0]:
                    break
                h[parent], h[i] = h[i], h[parent]
                i = parent

        def popHeap(h):
            retVal = h[0]
            endVal = h.pop()
            if not h:
                return retVal
            h[0] = endVal
            idx = 0
            size = len(h)
            while True:
                l = 2 * idx + 1
                r = 2 * idx + 2
                smallest = idx
                if l < size and h[l][0] < h[smallest][0]:
                    smallest = l
                if r < size and h[r][0] < h[smallest][0]:
                    smallest = r
                if smallest == idx:
                    break
                h[smallest], h[idx] = h[idx], h[smallest]
                idx = smallest
            return retVal

        a = createGraphMap()
        for q, r, s in edges:
            a[q].append((r, s))
            a[r].append((q, s))

        INF = 10**18
        b = [INF] * n
        b[0] = 0

        c = [(0, 0)]

        while c:
            m, t = popHeap(c)
            if m > b[t]:
                continue
            for y, z in a[t]:
                d = m + z
                if d < b[y]:
                    b[y] = d
                    pushHeap(c, (d, y))

        e = set()
        f = [(n - 1, b[n - 1])]
        g = [False] * n

        while f:
            j, k = f.pop()
            if g[j]:
                continue
            g[j] = True
            for l, m in a[j]:
                if k == b[l] + m:
                    u, v = j, l
                    if u > v:
                        u, v = v, u
                    e.add((u, v))
                    f.append((l, b[l]))

        h = []
        for o, p, _ in edges:
            x, y = o, p
            if x > y:
                x, y = y, x
            h.append((x, y) in e)

        return h