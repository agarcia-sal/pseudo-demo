from collections import deque

class Solution:
    def findWinningPlayer(self, skills, k):
        totalPlayers = len(skills)
        playerQueue = deque(range(totalPlayers))
        consecutiveWins = 0
        champion = playerQueue.popleft()

        while consecutiveWins < k and playerQueue:
            challenger = playerQueue.popleft()
            if skills[champion] > skills[challenger]:
                consecutiveWins += 1
                playerQueue.append(challenger)
            else:
                consecutiveWins = 1
                playerQueue.append(champion)
                champion = challenger

        return champion