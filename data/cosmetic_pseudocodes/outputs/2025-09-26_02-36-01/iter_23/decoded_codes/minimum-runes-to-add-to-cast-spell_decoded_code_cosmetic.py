from collections import defaultdict
from typing import List


class Solution:
    def minRunesToAdd(self, n: int, flowFrom: List[int], flowTo: List[int], crystals: List[int]) -> int:
        a1f = defaultdict(list)  # graph adjacency list: node -> list of neighbors
        z9b = defaultdict(list)  # reverse graph adjacency list: node -> list of predecessors

        def u7k(x2v, y1w, r8c, p5d, idx=0):
            if idx < len(x2v):
                q3e = x2v[idx]
                t0f = y1w[idx]
                if q3e not in r8c:
                    r8c[q3e] = []
                r8c[q3e].append(t0f)

                if t0f not in p5d:
                    p5d[t0f] = []
                p5d[t0f].append(q3e)

                u7k(x2v, y1w, r8c, p5d, idx + 1)

        u7k(flowFrom, flowTo, a1f, z9b, 0)

        z7k = [-1] * n  # discovery times (or ids)
        m8l = [0] * n   # low link values
        o1r = [False] * n  # on stack flags
        v0x = []  # stack
        y2g = 0   # time counter
        x8q = []  # list of strongly connected components (SCCs)

        def w3d(h6n):
            nonlocal y2g
            z7k[h6n] = y2g
            m8l[h6n] = y2g
            y2g += 1
            v0x.append(h6n)
            o1r[h6n] = True

            def iterateNeighbors(k9u=0):
                if k9u < len(a1f[h6n]):
                    j4t = a1f[h6n][k9u]
                    if z7k[j4t] == -1:
                        w3d(j4t)
                        if m8l[h6n] > m8l[j4t]:
                            m8l[h6n] = m8l[j4t]
                    else:
                        if o1r[j4t]:
                            if m8l[h6n] > z7k[j4t]:
                                m8l[h6n] = z7k[j4t]
                    iterateNeighbors(k9u + 1)

            iterateNeighbors()

            if m8l[h6n] == z7k[h6n]:
                r2s = []

                def extractStack():
                    if v0x:
                        w4m = v0x.pop()
                        o1r[w4m] = False
                        r2s.append(w4m)
                        if w4m != h6n:
                            extractStack()

                extractStack()
                x8q.append(r2s)

        def loopI(i=0):
            if i < n:
                if z7k[i] == -1:
                    w3d(i)
                loopI(i + 1)

        loopI()

        s0m = defaultdict(list)  # SCC graph adjacency list
        c3p = [-1] * n          # node to SCC id mapping
        e6z = [False] * len(x8q)  # SCC has crystal flag
        b9u = 0                  # SCC id counter

        def assignSCC(i=0, b9u_counter=0):
            if i < len(x8q):
                t5n = x8q[i]

                def assignNodes(j=0):
                    if j < len(t5n):
                        u7o = t5n[j]
                        c3p[u7o] = b9u_counter
                        if u7o in crystals:
                            e6z[i] = True
                        assignNodes(j + 1)

                assignNodes()
                assignSCC(i + 1, b9u_counter + 1)

        assignSCC()

        def buildSCCGraph(k=0):
            if k < len(flowFrom):
                o4v = flowFrom[k]
                d1x = flowTo[k]
                w2c = c3p[o4v]
                l7j = c3p[d1x]
                if w2c != l7j:
                    if l7j not in s0m[w2c]:
                        s0m[w2c].append(l7j)
                buildSCCGraph(k + 1)

        buildSCCGraph()

        p5y = [0] * len(x8q)  # indegree of SCC nodes

        def calculateIndegree(m=0):
            if m < len(x8q):
                if m in s0m:
                    def processNeighbors(n=0):
                        if n < len(s0m[m]):
                            z2h = s0m[m][n]
                            p5y[z2h] += 1
                            processNeighbors(n + 1)

                    processNeighbors()
                calculateIndegree(m + 1)

        calculateIndegree()

        g4r = 0

        def countAdditional(k1=0):
            nonlocal g4r
            if k1 < len(x8q):
                if p5y[k1] == 0 and not e6z[k1]:
                    g4r += 1
                countAdditional(k1 + 1)

        countAdditional()

        return g4r