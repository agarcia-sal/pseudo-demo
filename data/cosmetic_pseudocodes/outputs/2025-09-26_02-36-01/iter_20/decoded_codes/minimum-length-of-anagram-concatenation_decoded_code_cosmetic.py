class Solution:
    def minAnagramLength(self, t):
        def buildSet(x, r):
            if not x:
                return r
            else:
                k, l = x[0], x[1:]
                if k in r:
                    return buildSet(l, r)
                else:
                    r.add(k)
                    return buildSet(l, r)

        z = buildSet(list(t), set())

        def countElements(u):
            if not u:
                return 0
            else:
                return 1 + countElements(u[1:])

        y = countElements(list(z))
        return y