from collections import deque

class Solution:
    def findWinningPlayer(self, skills, k):
        total_players = len(skills)
        lineup = deque(range(total_players))
        consecutive_wins = 0
        champion = lineup.popleft()
        while consecutive_wins < k and len(lineup) > 0:
            contender = lineup.popleft()
            if skills[champion] > skills[contender]:
                consecutive_wins += 1
                lineup.append(contender)
            else:
                consecutive_wins = 1
                lineup.append(champion)
                champion = contender
        return champion