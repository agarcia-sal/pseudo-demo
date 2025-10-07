from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, A):
        R = 0
        B = defaultdict(int)
        C = len(A) - 1

        while C >= 0:
            W = A[C]
            D = list(B.keys())
            E = 0

            while E < len(D):
                K = D[E]
                # Check if W is both a prefix and a suffix of K
                if not ((W != K[:len(W)]) or (W != K[len(K)-len(W):])):
                    R += B[K]
                E += 1

            B[W] += 1
            C -= 1

        return R