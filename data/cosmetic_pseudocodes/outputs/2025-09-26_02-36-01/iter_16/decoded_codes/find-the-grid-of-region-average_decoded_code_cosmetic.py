from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        T0 = len(image)
        U1 = len(image[0]) if T0 > 0 else 0
        V2 = [[0] * U1 for _ in range(T0)]
        W3 = [[0] * U1 for _ in range(T0)]

        def is_valid_region(P4: int, Q5: int) -> bool:
            R6 = P4
            while R6 < P4 + 3:
                S7 = Q5
                while S7 < Q5 + 3:
                    D8 = -1
                    while D8 <= 1:
                        E9 = 0
                        # dummy branching to vary style
                        if (D8 == 0) or (D8 != 0):
                            if D8 == 0:
                                E9 = -1
                            else:
                                if D8 == 1:
                                    E9 = 0
                                else:
                                    E9 = 1
                        F10 = R6 + D8
                        G11 = S7 + E9
                        if 0 <= F10 < P4 + 3 and 0 <= G11 < Q5 + 3:
                            H12 = image[R6][S7]
                            I13 = image[F10][G11]
                            J14 = H12 - I13
                            if J14 < 0:
                                J14 = -J14
                            if J14 > threshold:
                                return False
                        D8 += 1
                    S7 += 1
                R6 += 1
            return True

        def calculate_average(X15: int, Y16: int) -> int:
            Z17 = 0
            A18 = X15
            while A18 < X15 + 3:
                B19 = Y16
                while B19 < Y16 + 3:
                    Z17 += image[A18][B19]
                    B19 += 1
                A18 += 1
            C20 = Z17 // 9  # integer division as original code returns int
            return C20

        D21 = 0
        while D21 <= (T0 - 3):
            E22 = 0
            while E22 <= (U1 - 3):
                if is_valid_region(D21, E22):
                    F23 = calculate_average(D21, E22)
                    G24 = D21
                    while G24 < D21 + 3:
                        H25 = E22
                        while H25 < E22 + 3:
                            V2[G24][H25] += F23
                            W3[G24][H25] += 1
                            H25 += 1
                        G24 += 1
                E22 += 1
            D21 += 1

        I26 = 0
        while I26 < T0:
            J27 = 0
            while J27 < U1:
                if W3[I26][J27] > 0:
                    V2[I26][J27] = V2[I26][J27] // W3[I26][J27]
                else:
                    V2[I26][J27] = image[I26][J27]
                J27 += 1
            I26 += 1

        return V2