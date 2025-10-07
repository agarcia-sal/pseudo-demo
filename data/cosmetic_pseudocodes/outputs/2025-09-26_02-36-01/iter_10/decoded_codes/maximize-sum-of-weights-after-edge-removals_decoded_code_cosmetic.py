class UnionFind:
    def __init__(self, size):
        self.parent = []
        self.rank = []
        idx = 0
        while idx < size:
            self.parent.append(idx)
            self.rank.append(0)
            idx += 1

    def find(self, u):
        def recurFind(x):
            if self.parent[x] == x:
                return x
            else:
                temp = recurFind(self.parent[x])
                self.parent[x] = temp
                return temp
        return recurFind(u)

    def union(self, u, v):
        ru = self.find(u)
        rv = self.find(v)
        if ru != rv:
            if self.rank[ru] > self.rank[rv]:
                self.parent[rv] = ru
            else:
                if self.rank[ru] < self.rank[rv]:
                    self.parent[ru] = rv
                else:
                    self.parent[rv] = ru
                    self.rank[ru] += 1


class Solution:
    def maximizeSumOfWeights(self, edges, k):
        def sortDescendingByThird(lst):
            if not lst or len(lst) == 1:
                return lst
            else:
                pivot = lst[0]
                leftPart = []
                rightPart = []
                i = 1
                while i < len(lst):
                    if lst[i][2] > pivot[2]:
                        leftPart.append(lst[i])
                    else:
                        rightPart.append(lst[i])
                    i += 1
                return sortDescendingByThird(leftPart) + [pivot] + sortDescendingByThird(rightPart)

        NPLUSONE = len(edges) + 1
        deg = [0] * NPLUSONE
        UFinstance = UnionFind(NPLUSONE)
        edgesSorted = sortDescendingByThird(edges)

        accSum = 0

        def processEdges(lst, pos):
            nonlocal accSum
            if pos == len(lst):
                return
            else:
                edgeVal = lst[pos]
                x1, x2, x3 = edgeVal[0], edgeVal[1], edgeVal[2]
                if deg[x1] < k and deg[x2] < k and UFinstance.find(x1) != UFinstance.find(x2):
                    UFinstance.union(x1, x2)
                    deg[x1] += 1
                    deg[x2] += 1
                    accSum += x3
                processEdges(lst, pos + 1)

        processEdges(edgesSorted, 0)
        return accSum