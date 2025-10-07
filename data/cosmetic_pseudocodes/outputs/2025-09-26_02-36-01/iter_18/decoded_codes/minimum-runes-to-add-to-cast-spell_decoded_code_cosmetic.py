from collections import defaultdict
from typing import List

class Solution:
    def minRunesToAdd(self, o1: List[int], s7: List[int], u2: List[int]) -> int:
        d3 = defaultdict(list)  # mapping from int to list of ints
        f6 = defaultdict(list)  # mapping from int to list of ints

        p0 = 0
        g4 = 0
        while p0 < len(o1) and g4 < len(s7):
            h8 = o1[p0]
            w5 = s7[g4]
            d3[h8].append(w5)
            f6[w5].append(h8)
            p0 += 1
            g4 += 1

        o2 = len(s7)  # number of unique vertices
        b7 = [-1] * o2
        e1 = [0] * o2
        r3 = [False] * o2
        m2 = []
        c8 = 0
        n4 = []

        def a9(z0: int):
            nonlocal c8
            b7[z0] = c8
            e1[z0] = c8
            c8 += 1
            m2.append(z0)
            r3[z0] = True

            v6 = 0
            while v6 < len(d3[z0]):
                l0 = d3[z0][v6]
                if b7[l0] == -1:
                    a9(l0)
                    if e1[z0] > e1[l0]:
                        e1[z0] = e1[l0]
                elif r3[l0]:
                    if e1[z0] > b7[l0]:
                        e1[z0] = b7[l0]
                v6 += 1

            if e1[z0] == b7[z0]:
                s8 = []
                while True:
                    u7 = m2.pop()
                    r3[u7] = False
                    s8.append(u7)
                    if u7 == z0:
                        break
                n4.append(s8)

        for j1 in range(o2):
            if b7[j1] == -1:
                a9(j1)

        y5 = defaultdict(list)
        g0 = [-1] * o2
        q9 = [False] * len(n4)
        t6 = 0

        for i7 in range(len(n4)):
            for x3 in n4[i7]:
                g0[x3] = t6
                if x3 in u2:
                    q9[i7] = True
            t6 += 1

        r9 = 0
        s0 = len(n4)
        while r9 < s0:
            k8 = 0
            while k8 < len(o1) and k8 < len(s7):
                h2 = g0[o1[k8]]
                p4 = g0[s7[k8]]
                if h2 != p4:
                    y5[h2].append(p4)
                k8 += 1
            r9 += 1

        w2 = [0] * s0

        j5 = 0
        while j5 < s0:
            if j5 in y5:
                for f0 in y5[j5]:
                    w2[f0] += 1
            j5 += 1

        m0 = 0
        c1 = 0
        while c1 < s0:
            if w2[c1] == 0 and not q9[c1]:
                m0 += 1
            c1 += 1

        return m0