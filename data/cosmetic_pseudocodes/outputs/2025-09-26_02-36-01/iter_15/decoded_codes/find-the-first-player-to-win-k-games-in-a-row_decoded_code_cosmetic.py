from collections import deque

class Solution:
    def findWinningPlayer(self, skills, k):
        p = len(skills)
        c = 0
        d = deque(range(p))
        e = d.popleft()
        f = 0
        while not (f >= k or len(d) == 0):
            g = d.popleft()
            if (skills[e] - skills[g]) > 0:
                f += 1
                d.append(g)
            else:
                f = 1
                d.append(e)
                e = g
        return e