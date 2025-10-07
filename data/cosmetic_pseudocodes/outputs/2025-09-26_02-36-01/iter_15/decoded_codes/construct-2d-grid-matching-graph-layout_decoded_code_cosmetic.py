from typing import List

class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        B = [[] for _ in range(n)]
        D = [-1] * 5

        for p, q in edges:
            B[p].append(q)
            B[q].append(p)

        for idx, nbrs in enumerate(B):
            deg_idx = len(nbrs)
            if 0 <= deg_idx < 5:
                D[deg_idx] = idx

        if D[1] != -1:
            S = [D[1]]
        elif D[4] == -1:
            M = D[2]
            S = []
            flag = False
            pos = 0
            while not flag and pos < len(B[M]):
                k = B[M][pos]
                if len(B[k]) == 2:
                    S = [M, k]
                    flag = True
                pos += 1
        else:
            M = D[2]
            S = [M]
            Prev = M
            Curr = B[M][0]

            while len(B[Curr]) > 2:
                S.append(Curr)
                found = False
                zdx = 0
                while not found and zdx < len(B[Curr]):
                    candidate = B[Curr][zdx]
                    if candidate != Prev and len(B[candidate]) < 4:
                        Prev = Curr
                        Curr = candidate
                        found = True
                    zdx += 1
            S.append(Curr)

        T = [S]
        checked = [False] * n
        R = 1
        loopLimit = (n // len(S)) - 1 if len(S) != 0 else 0  # avoid div by zero

        while R <= loopLimit:
            for el in S:
                checked[el] = True

            U = []
            for el in S:
                zz = 0
                while zz < len(B[el]):
                    nb = B[el][zz]
                    if not checked[nb]:
                        U.append(nb)
                        break
                    zz += 1
            T.append(U)
            S = U
            R += 1

        return T