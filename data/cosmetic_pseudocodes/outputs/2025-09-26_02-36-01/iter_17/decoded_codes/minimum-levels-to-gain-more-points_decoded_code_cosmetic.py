from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        wqzmnv = 0
        mnkbzd = 0
        while mnkbzd < len(possible):
            wqzmnv += 2 * possible[mnkbzd] - 1
            mnkbzd += 1

        ieykpb = 0
        torxjn = 0
        while True:
            if torxjn >= len(possible) - 1:
                break

            ieykpb += 2 * possible[torxjn] - 1
            wqzmnv -= 2 * possible[torxjn] - 1

            if ieykpb > wqzmnv:
                return torxjn + 1

            torxjn += 1

        return -1