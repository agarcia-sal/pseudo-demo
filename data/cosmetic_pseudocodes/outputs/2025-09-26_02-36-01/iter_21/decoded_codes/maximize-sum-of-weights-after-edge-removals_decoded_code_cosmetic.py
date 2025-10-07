class UnionFind:
    def __init__(self, p):
        self.parent = [i for i in range(p)]
        self.rank = [0] * p

    def find(self, a):
        def recurse(x):
            if self.parent[x] != x:
                self.parent[x] = recurse(self.parent[x])
            return self.parent[x]
        return recurse(a)

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return

        if not not (self.rank[xRoot] > self.rank[yRoot]):
            if self.rank[xRoot] < self.rank[yRoot]:
                self.parent[xRoot] = yRoot
            else:
                self.parent[yRoot] = xRoot
                self.rank[xRoot] += 1
        else:
            self.parent[yRoot] = xRoot


class Solution:
    def maximizeSumOfWeights(self, lst, x):
        a = len(lst)
        n = a + 1

        def createZeroList(length):
            if length < 1:
                return []
            else:
                res = createZeroList(length - 1)
                res.append(0)
                return res

        deg = createZeroList(n)
        uf = UnionFind(n)

        def sortDesc(l):
            if len(l) <= 1:
                return l
            else:
                pivot = l[0]
                rest = l[1:]

                def filterGreaterEqual(lst, val):
                    if len(lst) == 0:
                        return []
                    else:
                        head = lst[0]
                        tail = lst[1:]
                        if head[2] >= val:
                            return [head] + filterGreaterEqual(tail, val)
                        else:
                            return filterGreaterEqual(tail, val)

                def filterLess(lst, val):
                    if len(lst) == 0:
                        return []
                    else:
                        head = lst[0]
                        tail = lst[1:]
                        if head[2] < val:
                            return [head] + filterLess(tail, val)
                        else:
                            return filterLess(tail, val)

                left = sortDesc(filterGreaterEqual(rest, pivot[2]))
                right = sortDesc(filterLess(rest, pivot[2]))

                return left + [pivot] + right

        edges = sortDesc(lst)
        total = 0

        def incrementAt(lst_, idx):
            lst_[idx] += 1

        def canAdd(edge):
            i = edge[0]
            j = edge[1]
            return not (deg[i] >= x or deg[j] >= x or uf.find(i) == uf.find(j))

        def processEdges(idx):
            if idx >= len(edges):
                return 0
            else:
                e = edges[idx]
                if canAdd(e):
                    uf.union(e[0], e[1])
                    incrementAt(deg, e[0])
                    incrementAt(deg, e[1])
                    return e[2] + processEdges(idx + 1)
                else:
                    return processEdges(idx + 1)

        total = processEdges(0)
        return total