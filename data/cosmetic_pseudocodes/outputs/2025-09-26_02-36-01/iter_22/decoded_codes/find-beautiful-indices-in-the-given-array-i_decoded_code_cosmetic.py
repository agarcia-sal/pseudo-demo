class Solution:
    def beautifulIndices(self, s, a, b, k):
        R1 = []
        limit_a = len(s) - len(a) + 1
        for X1 in range(limit_a):
            F1 = True
            for M1 in range(len(a)):
                if s[X1 + M1] != a[M1]:
                    F1 = False
                    break
            if F1:
                R1.append(X1)

        R2 = []
        limit_b = len(s) - len(b) + 1
        for X2 in range(limit_b):
            F2 = True
            for M2 in range(len(b)):
                if s[X2 + M2] != b[M2]:
                    F2 = False
                    break
            if F2:
                R2.append(X2)

        V = []
        for I in R1:
            for J in R2:
                if -k <= (I - J) <= k:
                    V.append(I)
                    break

        return V