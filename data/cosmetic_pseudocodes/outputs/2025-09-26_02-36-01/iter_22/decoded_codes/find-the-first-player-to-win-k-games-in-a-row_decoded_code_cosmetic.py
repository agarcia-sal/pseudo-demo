class Solution:
    def findWinningPlayer(self, skills, k):
        totalPlayers = len(skills)
        line = list(range(totalPlayers))
        streak = 0
        champ = self.popFront(line)
        while streak < k and len(line) > 0:
            contender = self.popFront(line)
            if skills[champ] > skills[contender]:
                streak += 1
                line.append(contender)
            else:
                streak = 1
                line.append(champ)
                champ = contender
        return champ

    def popFront(self, arr):
        frontElem = arr[0]
        del arr[0]
        return frontElem