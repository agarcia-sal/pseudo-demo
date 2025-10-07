from collections import defaultdict, deque

class Solution:
    def minRunesToAdd(self, n, flowFrom, flowTo, crystals):
        p = defaultdict(list)  # adjacency list for original graph

        for u, v in zip(flowFrom, flowTo):
            p[u].append(v)

        v = [-1] * n  # discovery times
        z = [0] * n   # low-link values
        a = [False] * n  # on stack flags
        y = []  # stack
        w = 0   # time counter
        s = []  # list of SCCs

        def u(x):
            nonlocal w
            v[x] = w
            z[x] = w
            w += 1
            y.append(x)
            a[x] = True

            for c in p[x]:
                if v[c] == -1:
                    u(c)
                    if z[x] > z[c]:
                        z[x] = z[c]
                elif a[c]:
                    if z[x] > v[c]:
                        z[x] = v[c]

            if z[x] == v[x]:
                k = []
                while True:
                    h = y.pop()
                    a[h] = False
                    k.append(h)
                    if h == x:
                        break
                s.append(k)

        for i in range(n):
            if v[i] == -1:
                u(i)

        m = defaultdict(list)  # adjacency of component graph
        d = [-1] * n           # component id for each node
        e = [False] * len(s)   # does component contain crystal
        f = 0                  # component index

        # assign component ids and mark crystals
        for j, comp in enumerate(s):
            for l in comp:
                d[l] = j
                if l in crystals:
                    e[j] = True

        for o in range(len(flowFrom)):
            x_comp = d[flowFrom[o]]
            y_comp = d[flowTo[o]]
            if x_comp != y_comp:
                m[x_comp].append(y_comp)

        c = [0] * len(s)  # in-degree count for components

        for q_idx in range(len(s)):
            for r in m[q_idx]:
                c[r] += 1

        b = 0
        for n_idx in range(len(s)):
            if c[n_idx] == 0 and not e[n_idx]:
                b += 1

        return b