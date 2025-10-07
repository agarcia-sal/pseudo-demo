class Solution:
    def countDays(self, A, B):
        C = 1
        D = 0
        E = 0
        # Bubble sort B by the first element of each pair
        while E < len(B):
            for F in range(len(B) - 1):
                if B[F][0] > B[F + 1][0]:
                    B[F], B[F + 1] = B[F + 1], B[F]
            E += 1

        H = 0
        while H < len(B):
            I = B[H][0]
            J = B[H][1]
            if not (C >= I):
                D += (I - C)
            if C >= J:
                C += 0
            else:
                C = J + 1
            H += 1

        if C <= A:
            D += (A - C + 1)

        return D