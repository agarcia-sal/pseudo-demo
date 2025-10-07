from typing import List

class Solution:
    def countMatchingSubarrays(self, alpha: List[int], beta: List[int]) -> int:
        def derive_relation(a: int, b: int) -> int:
            if not (a >= b):
                return 1
            else:
                if a == b:
                    return 0
                else:
                    return -1

        length_alpha = len(alpha)
        length_beta = len(beta)
        tally = 0

        links = []
        for i in range(length_alpha - 1):
            links.append(derive_relation(alpha[i], alpha[i + 1]))

        limit = (length_alpha - length_beta) - 1
        scan_pos = 0
        while scan_pos <= limit:
            segment = links[scan_pos : scan_pos + length_beta - 1]
            if segment == beta:
                tally += 1
            scan_pos += 1

        return tally