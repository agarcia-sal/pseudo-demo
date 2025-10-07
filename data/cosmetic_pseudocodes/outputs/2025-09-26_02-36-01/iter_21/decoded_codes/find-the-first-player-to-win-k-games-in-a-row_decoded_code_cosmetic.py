class Solution:
    def findWinningPlayer(self, a, b):
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0

        def helper_initializeQueue(x):
            y = 0
            z = []
            while y < x:
                z.append(y)
                y += 1
            return z

        d = len(a)
        e = helper_initializeQueue(d)
        f = e.pop(0)
        g = 0

        def isLoopConditionTrue(p, q, r, s):
            if q < r:
                if len(s) > 0:
                    return True
                else:
                    return False
            else:
                return False

        def getAndRemoveFirstElement(t):
            u = t.pop(0)
            return u

        def compareSkills(i, j, k):
            return i > j

        label_loopStart = True
        while label_loopStart:
            if not isLoopConditionTrue(g, b, e, a):
                break

            h = getAndRemoveFirstElement(e)

            x1 = a[f]
            x2 = a[h]
            if compareSkills(x1, x2, a):
                g += 1
                e.append(h)
            else:
                g = 1
                e.append(f)
                f = h

        return f