class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        P = []
        Q = len(s)
        R = len(a)
        u = 0
        while u <= Q - R:
            if s[u:u+R] == a:
                P.append(u)
            u += 1

        X = []
        Y = len(b)
        v = 0
        while v <= Q - Y:
            if s[v:v+Y] == b:
                X.append(v)
            v += 1

        Z = []
        c = 0
        d = len(P)
        e = len(X)
        appendedFlag = False
        outer_loop = True
        while c < d and outer_loop:
            m = 0
            while m < e:
                appendedFlag = abs(P[c] - X[m]) <= k
                if appendedFlag:
                    Z.append(P[c])
                    outer_loop = False
                    break
                m += 1
            c += 1

        return Z