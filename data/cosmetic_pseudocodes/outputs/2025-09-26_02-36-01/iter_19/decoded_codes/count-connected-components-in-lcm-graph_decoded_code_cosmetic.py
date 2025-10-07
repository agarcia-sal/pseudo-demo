class DSU:
    def __init__(self, z):
        self.parent = {}
        self.rank = {}
        c = 0
        while c < z:
            self.parent[c] = c
            self.rank[c] = 0
            c += 1

    def find(self, y):
        retVal = self.parent[y]
        if retVal != y:
            self.parent[y] = self.find(self.parent[y])
        return self.parent[y]

    def union_set(self, a, b):
        x = self.find(a)
        w = self.find(b)
        if x != w:
            if self.rank[x] < self.rank[w]:
                x, w = w, x
            self.parent[w] = x
            if self.rank[x] == self.rank[w]:
                self.rank[x] += 1


class Solution:
    def countComponents(self, arr, lim):
        dsuInstance = DSU(lim + 1)
        outerIndex = 0
        while outerIndex < len(arr):
            currentNum = arr[outerIndex]
            innerVal = currentNum * 2
            while innerVal <= lim:
                dsuInstance.union_set(currentNum, innerVal)
                innerVal += currentNum
            outerIndex += 1

        parentsSet = set()
        idx = 0
        while idx < len(arr):
            numValue = arr[idx]
            if numValue <= lim:
                parId = dsuInstance.find(numValue)
                parentsSet.add(parId)
            else:
                parentsSet.add(numValue)
            idx += 1
        return len(parentsSet)