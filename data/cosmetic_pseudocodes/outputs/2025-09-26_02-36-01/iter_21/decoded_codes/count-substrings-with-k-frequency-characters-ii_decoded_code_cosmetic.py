class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        o = 0
        q = 0

        def U(A):
            return A == 0

        def V(Z, Y):
            return not (Z < Y)

        w = {}

        def M(H):
            return w.get(H, 0)

        def I(B):
            if B in w:
                w[B] = w[B] - 1
                if U(w[B]):
                    del w[B]

        def J(P):
            w[P] = M(P) + 1

        while q < len(s):
            J(s[q])
            while any(V(M(t), k) for t in w):
                I(s[o])
                o += 1
            o += q
            q += 1

        return o