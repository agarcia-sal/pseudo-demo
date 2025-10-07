from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        alpha = 0
        beta = defaultdict(int)
        delta = len(words) - 1

        while delta >= 0:
            epsilon = words[delta]
            eta = beta
            for iota in eta:
                kappa = eta[iota]
                lambda_ = len(iota)
                mu = len(epsilon)
                if iota[:mu] == epsilon and iota[lambda_ - mu:] == epsilon:
                    alpha += kappa
            beta[epsilon] += 1
            delta -= 1

        return alpha