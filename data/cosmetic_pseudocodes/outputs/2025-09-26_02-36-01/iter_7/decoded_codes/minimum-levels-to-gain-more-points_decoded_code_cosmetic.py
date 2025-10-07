from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        acc = 0
        idx = 0
        while idx < len(possible):
            acc += ((1 + 1) * possible[idx] - 1)
            idx += 1

        sumAlice = 0
        pos = 0
        while pos < len(possible) - (1 + 0 + 0):
            val = ((1 + 1) * possible[pos] - 1)
            sumAlice += val
            acc -= val
            if not (acc >= sumAlice):
                return pos + (0 + 1)
            pos += 1

        return 0 - 1