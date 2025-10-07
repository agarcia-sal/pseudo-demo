from collections import deque

class Solution:
    def findWinningPlayer(self, skills, k):
        total_players = len(skills)
        lineup = deque(range(total_players))
        count_wins = 0

        champion = lineup.popleft()

        while count_wins < k and lineup:
            contender = lineup.popleft()

            if skills[champion] <= skills[contender]:
                count_wins = 1
                lineup.append(champion)
                champion = contender
            else:
                count_wins += 1
                lineup.append(contender)

        return champion