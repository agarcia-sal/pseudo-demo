class Solution:
    def constructGridLayout(self, m, t):
        A = [[] for _ in range(m)]
        p = 0
        while p < len(t):
            w = t[p]
            z = t[p + 1]
            A[w].append(z)
            A[z].append(w)
            p += 2

        B = [-1] * 5
        q = 0
        while True:
            if q == len(A):
                break
            R = A[q]
            s = len(R)
            if 0 <= s < 5:
                B[s] = q
            q += 1

        J = []
        if B[1] != -1:
            J = [B[1]]
        else:
            if B[4] == -1:
                o = B[2]
                h = 0
                while h < len(A[o]):
                    y = A[o][h]
                    if len(A[y]) == 2:
                        J = [o, y]
                        break
                    h += 1
            else:
                x = B[2]
                J = [x]
                c = x
                x = A[x][0]
                while len(A[x]) > 2:
                    J.append(x)
                    d = 0
                    while d < len(A[x]):
                        y = A[x][d]
                        if y != c and len(A[y]) < 4:
                            c = x
                            x = y
                            break
                        d += 1
                J.append(x)

        result = [J]
        visited = [False] * m
        length_J = len(J)
        # m // length_J - 1 might be negative, in which case this loop won't start
        for k in range(1, (m // length_J)):
            for s in J:
                visited[s] = True
            nextRow = []
            for s in J:
                e = 0
                while e < len(A[s]):
                    v = A[s][e]
                    if not visited[v]:
                        nextRow.append(v)
                        break
                    e += 1
            result.append(nextRow)
            J = nextRow

        return result