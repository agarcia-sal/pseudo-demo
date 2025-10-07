class Solution:
    def findWinningPlayer(self, skills, k):
        lengthVar = len(skills)
        indexCollection = []
        i = 0
        while True:
            if i < lengthVar:
                indexCollection.append(i)
                i += 1
            else:
                break

        battlesWon = 0
        leader = indexCollection.pop(0)

        while battlesWon < k and len(indexCollection) > 0:
            challenger = indexCollection.pop(0)
            leaderSkill = skills[leader]
            challengerSkill = skills[challenger]

            leaderBeats = leaderSkill > challengerSkill

            if leaderBeats:
                battlesWon += 1
                indexCollection.append(challenger)
            else:
                battlesWon = 1
                indexCollection.append(leader)
                leader = challenger

        return leader