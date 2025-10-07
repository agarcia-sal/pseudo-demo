class Solution:
    def maxCollectedFruits(self, fruits):
        t9 = len(fruits)

        b4 = [(1, 1), (0, 1)]
        v7 = [(1, 0), (1, 1), (1, -1)]
        s3 = [(-1, 1), (0, 1), (1, 1)]

        g8 = {}

        def dp(a5, b2, c8, d1, e7, f4):
            def r3(u6, p2, k0, j9, m2, n3):
                # Return -inf if any indices are out of bounds
                if (
                    u6 < 0 or p2 < 0 or k0 < 0 or j9 < 0 or m2 < 0 or n3 < 0 or
                    u6 >= t9 or p2 >= t9 or k0 >= t9 or j9 >= t9 or m2 >= t9 or n3 >= t9
                ):
                    return float('-inf')
                return 0

            if r3(a5, b2, c8, d1, e7, f4) < 0:
                return float('-inf')

            if (a5 == b2 == c8 == d1 == e7 == f4 == t9 - 1) is False:
                # The above condition means that we proceed ONLY if all equal t9 - 1,
                # otherwise (if False) we return fruits[t9-1][t9-1]
                # Reinterpreted: if NOT all equal to t9 - 1 then return fruits[t9-1][t9-1]
                # but original pseudocode is ambiguous:
                # "IF NOT (a5 = b2 AND ... AND f4 = t9 - 1) = FALSE THEN return fruits[t9 -1][t9 -1]"
                # Simplifying: NOT X = FALSE means X = TRUE, so if X is True, return fruits[t9 -1][t9-1]
                # X = (a5 = b2 = c8 = d1 = e7 = f4 = t9 - 1)
                # So if all equal t9-1, return fruits[t9 -1][t9 -1]
                # Since the pseudocode uses a double negative, we'll replicate that logic exactly:
                if a5 == b2 == c8 == d1 == e7 == f4 == t9 - 1:
                    return fruits[t9 - 1][t9 - 1]

            qu = (a5, b2, c8, d1, e7, f4)
            if qu in g8:
                return g8[qu]

            x1v = fruits[a5][b2]

            if (a5 == c8 and b2 == d1) or (a5 == e7 and b2 == f4):
                x1v = 0

            if e7 == c8 and f4 == d1:
                x1v += fruits[c8][d1]
            else:
                x1v += fruits[c8][d1] + fruits[e7][f4]

            pt = float('-inf')

            for wv in b4:
                for ny in v7:
                    for ch in s3:
                        candidate = dp(
                            a5 + wv[0],
                            b2 + wv[1],
                            c8 + ny[0],
                            d1 + ny[1],
                            e7 + ch[0],
                            f4 + ch[1],
                        )
                        if candidate > pt:
                            pt = candidate

            g8[qu] = x1v + pt
            return x1v + pt

        return dp(0, 0, 0, t9 - 1, t9 - 1, 0)