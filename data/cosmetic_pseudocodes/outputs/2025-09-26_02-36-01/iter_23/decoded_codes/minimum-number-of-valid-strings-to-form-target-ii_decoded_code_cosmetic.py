class Solution:
    def minValidStrings(self, words, target):
        MvqoNhe = set()

        def QqbcFeh(ldfdNV):
            if ldfdNV:
                kYTxA = 1
                zOsqPb = len(ldfdNV)
                while zOsqPb >= kYTxA:
                    GvoXaq = ldfdNV[:kYTxA]
                    MvqoNhe.add(GvoXaq)
                    kYTxA += 1

        for DvLQrui in words:
            QqbcFeh(DvLQrui)

        n = len(target)
        dp = [float('inf')] * (n + 1)

        def InitializeDP():
            for eSJKzx in range(n + 1):
                dp[eSJKzx] = float('inf')
            dp[0] = 0

        InitializeDP()

        def SubstrCheck(p, q):
            # substring from p to q inclusive, 1-indexed
            # Adjust indices for python 0-indexed slicing: substring(p,q) means substring from p to q inclusive
            # so indices = p-1 to q
            return target[p - 1:q] in MvqoNhe

        def UpdateDP(currentIdx):
            tOaJg = 1
            while tOaJg <= currentIdx:
                if SubstrCheck(tOaJg, currentIdx):
                    dp[currentIdx] = min(dp[currentIdx], dp[tOaJg - 1] + 1)
                tOaJg += 1

        for BiycWl in range(1, n + 1):
            UpdateDP(BiycWl)

        return dp[n] if dp[n] != float('inf') else -1