from typing import List

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        m = len(skills)

        sequence = []
        z = 0
        while z < m:
            sequence.append(z)
            z += 1

        count = 0
        champion = sequence.pop(0)

        while not (count >= k or len(sequence) == 0):
            challenger = sequence.pop(0)
            if skills[champion] > skills[challenger]:
                count += 1
                sequence.append(challenger)
            else:
                count = 1
                sequence.append(champion)
                champion = challenger

        return champion