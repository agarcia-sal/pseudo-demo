class Solution:
    def findWinningPlayer(self, skills, k):
        m = len(skills)
        ensemble = list(range(m))

        tally = 0
        leader = ensemble.pop(0)

        while tally < k and len(ensemble) > 0:
            contender = ensemble.pop(0)
            if skills[leader] > skills[contender]:
                tally += 1
                ensemble.append(contender)
            else:
                tally = 1
                ensemble.append(leader)
                leader = contender

        return leader