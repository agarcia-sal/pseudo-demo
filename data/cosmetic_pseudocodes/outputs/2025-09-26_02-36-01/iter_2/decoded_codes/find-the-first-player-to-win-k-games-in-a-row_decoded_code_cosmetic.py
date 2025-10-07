from collections import deque

class Solution:
    def findWinningPlayer(self, skills, k):
        total_players = len(skills)
        lineup = deque(range(total_players))
        score_streak = 0
        champion = lineup.popleft()

        while score_streak < k and lineup:
            challenger = lineup.popleft()
            if skills[champion] > skills[challenger]:
                score_streak += 1
                lineup.append(challenger)
            else:
                score_streak = 1
                lineup.append(champion)
                champion = challenger

        return champion