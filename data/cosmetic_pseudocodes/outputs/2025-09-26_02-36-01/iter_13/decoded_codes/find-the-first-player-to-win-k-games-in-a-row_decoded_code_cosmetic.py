from collections import deque

class Solution:
    def findWinningPlayer(self, skillList, threshold):
        totalPlayers = len(skillList)
        playerQueue = deque()

        def buildQueue(index, limit):
            if index == limit:
                return
            playerQueue.append(index)
            buildQueue(index + 1, limit)

        buildQueue(0, totalPlayers)

        consecutiveWins = 0
        champion = playerQueue.popleft()

        def competitionCycle():
            nonlocal consecutiveWins, champion
            if consecutiveWins >= threshold or not playerQueue:
                return
            challenger = playerQueue.popleft()
            if skillList[champion] > skillList[challenger]:
                consecutiveWins += 1
                playerQueue.append(challenger)
            else:
                consecutiveWins = 1
                playerQueue.append(champion)
                champion = challenger
            competitionCycle()

        competitionCycle()
        return champion