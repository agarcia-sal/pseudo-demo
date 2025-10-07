from collections import Counter

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        alpha = 0
        omega = len(word)
        lambda_list = []

        while alpha < omega:
            beta = word[alpha:alpha + k]
            lambda_list.append(beta)
            alpha += k

        def customCountDuplicates(arr):
            tally = {}
            for theta in arr:
                if theta in tally:
                    tally[theta] += 1
                else:
                    tally[theta] = 1
            return tally

        hash_map = customCountDuplicates(lambda_list)

        delta = 0
        for gamma, sigma in hash_map.items():
            if sigma > delta:
                delta = sigma

        epsilon = len(lambda_list) - delta
        return epsilon