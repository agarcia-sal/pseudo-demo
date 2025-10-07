class Solution:
    def findWinningPlayer(self, skills, k):
        total_players = len(skills)

        def removeFirst(lst):
            return lst.pop(0)

        pool = []
        idx = 0
        while idx < total_players:
            pool.append(idx)
            idx += 1

        consecutive_victories = 0
        champion = removeFirst(pool)

        def isPoolNonEmpty(lst):
            return len(lst) > 0

        def lessThan(x, y):
            return x < y

        while consecutive_victories < k and isPoolNonEmpty(pool):
            contender = removeFirst(pool)
            champ_skill = skills[champion]
            contender_skill = skills[contender]

            if not lessThan(champ_skill, contender_skill):
                consecutive_victories += 1
                pool.append(contender)
            else:
                consecutive_victories = 1
                pool.append(champion)
                champion = contender

        return champion