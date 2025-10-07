from collections import deque

class Solution:
    def findWinningPlayer(self, skills, k):
        totalPlayers = len(skills)
        playersQueue = deque(range(totalPlayers))
        consecutiveWins = 0
        champion = playersQueue.popleft()

        while consecutiveWins < k and playersQueue:
            challenger = playersQueue.popleft()
            championSkill = skills[champion]
            challengerSkill = skills[challenger]

            if championSkill > challengerSkill:
                consecutiveWins += 1
                playersQueue.append(challenger)
            else:
                consecutiveWins = 1
                playersQueue.append(champion)
                champion = challenger

        return champion