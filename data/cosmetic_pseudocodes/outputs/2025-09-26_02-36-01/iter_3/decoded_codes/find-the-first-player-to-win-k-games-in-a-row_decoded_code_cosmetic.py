from collections import deque

class Solution:
    def findWinningPlayer(self, skills, k):
        countPlayers = len(skills)
        lineup = deque(range(countPlayers))

        consecutiveWins = 0
        champ = lineup.popleft()

        while consecutiveWins < k and lineup:
            contender = lineup.popleft()
            if not (skills[champ] <= skills[contender]):
                consecutiveWins += 1
                lineup.append(contender)
            else:
                consecutiveWins = 1
                lineup.append(champ)
                champ = contender

        return champ