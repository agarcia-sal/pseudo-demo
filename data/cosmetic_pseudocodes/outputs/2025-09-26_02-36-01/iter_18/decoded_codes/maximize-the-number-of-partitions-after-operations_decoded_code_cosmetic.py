class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(q: str, r: int) -> int:
            alpha = set()
            beta = 0
            omega = 0
            while omega < len(q):
                delta = q[omega]
                if delta not in alpha:
                    if len(alpha) >= r:
                        beta += 1
                        alpha = {delta}
                    else:
                        alpha.add(delta)
                omega += 1
            if len(alpha) != 0:
                beta += 1
            return beta

        sigma = max_partitions(s, k)
        tau = 0
        while tau <= len(s) -1:
            mu = 'a'
            while mu <= 'z':
                if mu == s[tau]:
                    mu = chr(ord(mu) + 1)
                    continue
                # build new string with mu replacing s[tau]
                lambd = s[:tau] + mu + s[tau+1:]
                sigma = max(sigma, max_partitions(lambd, k))
                mu = chr(ord(mu) + 1)
            tau += 1
        return sigma