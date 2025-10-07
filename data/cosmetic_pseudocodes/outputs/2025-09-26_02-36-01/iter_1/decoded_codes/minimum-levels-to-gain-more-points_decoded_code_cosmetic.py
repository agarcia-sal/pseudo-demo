from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        sum_points = 0
        for value in possible:
            sum_points += 2 * value - 1

        alice_score = 0
        for i in range(len(possible) - 1):
            alice_score += 2 * possible[i] - 1
            sum_points -= 2 * possible[i] - 1

            if alice_score > sum_points:
                return i + 1

        return -1