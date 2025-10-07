from typing import List

class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        A = [[] for _ in range(n)]
        B = 0
        while B < len(edges):
            C = edges[B]
            D, E = C[0], C[1]
            A[D].append(E)
            A[E].append(D)
            B += 1

        F = [-1] * 5
        G = 0
        while True:
            if G >= len(A):
                break
            H = A[G]
            I = len(H)
            if I < 5:
                F[I] = G
            G += 1

        J = F[1]
        K = -1
        if J != K:
            L = [J]
        else:
            if F[4] == K:
                M = F[2]
                L = []
                for N in range(len(A[M])):
                    O = A[M][N]
                    if len(A[O]) == 2:
                        L = [M, O]
                        break
            else:
                P = F[2]
                L = [P]
                Q = P
                R = A[P][0]
                S = True
                while S:
                    if len(A[R]) <= 2:
                        S = False
                    else:
                        L.append(R)
                        T = 0
                        U = False
                        while not U and T < len(A[R]):
                            V = A[R][T]
                            if V != Q and len(A[V]) < 4:
                                Q = R
                                R = V
                                U = True
                            T += 1
                L.append(R)

        W = [L]
        X = [False] * n
        Y = 0
        Z = (n // len(L)) - 1
        while True:
            if Y > Z:
                break
            for AB in L:
                X[AB] = True

            AC = []
            for AE in L:
                AF = 0
                AG = False
                edges_AE = A[AE]
                while not AG and AF < len(edges_AE):
                    AH = edges_AE[AF]
                    if not X[AH]:
                        AC.append(AH)
                        AG = True
                    AF += 1

            W.append(AC)
            L = AC
            Y += 1

        return W