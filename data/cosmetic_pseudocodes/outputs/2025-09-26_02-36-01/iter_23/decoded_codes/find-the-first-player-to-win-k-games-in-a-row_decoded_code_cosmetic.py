class Solution:
    def findWinningPlayer(self, skills, k):
        size = len(skills)

        def dequeueFirst(L):
            firstElem = L[0]
            del L[0]
            return firstElem

        idxQueue = []
        iterIndex = 0
        while iterIndex < size:
            idxQueue.append(iterIndex)
            iterIndex += 1

        countWins = 0
        champ = dequeueFirst(idxQueue)

        def conditionCheck(winsVal, qList):
            return winsVal >= k or len(qList) == 0

        while not conditionCheck(countWins, idxQueue):
            challenger = dequeueFirst(idxQueue)
            if skills[champ] - skills[challenger] > 0:
                countWins += 1
                idxQueue.append(challenger)
            else:
                countWins = 1
                idxQueue.append(champ)
                champ = challenger

        return champ