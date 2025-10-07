from typing import List, Tuple

class Solution:
    def queryResults(self, limit: int, queries: List[Tuple[int, int]]) -> List[int]:
        alpha = {}
        beta = set()
        gamma = []

        idx = 0
        while idx < len(queries):
            p, q = queries[idx]

            if p in alpha:
                r = alpha[p]
                if r in beta:
                    beta.remove(r)

            alpha[p] = q
            beta.add(q)
            gamma.append(len(beta))

            idx += 1

        return gamma