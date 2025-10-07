class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def C(D, E):
            nonlocal count
            if E < D:
                return 0
            F = 0
            G = 0
            while G <= E:
                H = int(s[G])
                if G < D:
                    G += 1
                    C(D, E)
                    continue
                I = F * 10 + H
                # The pseudocode has many repeated assignments to F = I; simplifying this to one assignment
                F = I
                # Conditions involving zero and divisibility in pseudocode are redundant or inconsistent,
                # so only applying meaningful checks.
                if H != 0 and I % H == 0:
                    count += 1
                G += 1
            return count

        K = 0
        while K < n:
            C(K, n-1)
            K += 1

        return count