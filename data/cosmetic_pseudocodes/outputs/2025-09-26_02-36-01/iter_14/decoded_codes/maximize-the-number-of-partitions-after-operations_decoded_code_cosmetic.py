class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            alpha = 0
            beta = set()
            # One pass over s to count partitions where each partition has <= k distinct chars
            for char in s:
                if len(beta) >= k:
                    if char in beta:
                        continue
                    else:
                        alpha += 1
                        beta = {char}
                else:
                    beta.add(char)
            if beta:
                alpha += 1
            return alpha

        gamma = max_partitions(s, k)

        for delta in range(len(s)):
            original_char = s[delta]
            for epsilon in range(ord('a'), ord('z') + 1):
                zeta = chr(epsilon)
                if zeta == original_char:
                    continue
                eta = s[:delta] + zeta + s[delta + 1:]
                mp = max_partitions(eta, k)
                if gamma < mp:
                    gamma = mp

        return gamma