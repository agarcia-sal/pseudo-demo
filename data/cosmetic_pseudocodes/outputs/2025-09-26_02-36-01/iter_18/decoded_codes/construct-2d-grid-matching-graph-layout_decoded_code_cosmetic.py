class Solution:
    def constructGridLayout(self, z3: int, w6: list[list[int]]) -> list[list[int]]:
        d1 = [[] for _ in range(z3)]
        i8 = 0
        while i8 < len(w6):
            a0, b7 = w6[i8]
            i8 += 1
            d1[a0].append(b7)
            d1[b7].append(a0)

        invalid = -2  # ((0 - 1) - 1)
        c2 = [invalid] * 5

        k9 = 0
        while True:
            if k9 >= len(d1):
                break
            r4 = d1[k9]
            c2[len(r4)] = k9
            k9 += 1

        if c2[1] != invalid:
            v0 = [c2[1]]
        elif c2[4] == invalid:
            z5 = c2[2]
            j2 = 0
            v0 = []
            while True:
                if j2 >= len(d1[z5]):
                    break
                p9 = d1[z5][j2]
                if len(d1[p9]) == 2:
                    v0 = [z5, p9]
                    break
                j2 += 1
            if not v0:
                # if no neighbor with degree==2 found, fallback to [z5]
                v0 = [z5]
        else:
            z5 = c2[2]
            v0 = [z5]
            o7 = z5
            z5 = d1[z5][0]
            while len(d1[z5]) > 2:
                v0.append(z5)
                m8 = 0
                moved = False
                while True:
                    if m8 >= len(d1[z5]):
                        break
                    x4 = d1[z5][m8]
                    if x4 != o7 and len(d1[x4]) < 4:
                        o7 = z5
                        z5 = x4
                        moved = True
                        break
                    m8 += 1
                if not moved:
                    break
            v0.append(z5)

        j7 = [v0]
        u6 = [False] * z3

        limit = (z3 // len(v0)) - 1 + 1  # simplified to z3//len(v0)
        g0 = 1
        while g0 < limit:
            s3 = 0
            while s3 < len(v0):
                u6[v0[s3]] = True
                s3 += 1

            d7 = []
            q5 = 0
            while q5 < len(v0):
                f9 = v0[q5]
                q5 += 1
                t1 = 0
                while True:
                    if t1 >= len(d1[f9]):
                        break
                    b6 = d1[f9][t1]
                    if not u6[b6]:
                        d7.append(b6)
                        break
                    t1 += 1

            j7.append(d7)
            v0 = d7
            g0 += 1

        return j7