class DSU:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}

    def find(self, x):
        def recursiveFind(y):
            if self.parent[y] != y:
                self.parent[y] = recursiveFind(self.parent[y])
            return self.parent[y]
        return recursiveFind(x)

    def union_set(self, u, v):
        def swapIfNeeded(a, b):
            if self.rank[a] < self.rank[b]:
                return b, a
            else:
                return a, b

        u = self.find(u)
        v = self.find(v)
        if u != v:
            u, v = swapIfNeeded(u, v)
            self.parent[v] = u
            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1


class Solution:
    def countComponents(self, nums, threshold):
        def generateMultiples(base, limit):
            multiplesList = []
            currVal = base + base
            while currVal <= limit:
                multiplesList.append(currVal)
                currVal += base
            return multiplesList

        dsu = DSU(threshold + 1)

        outerIndex = 0
        nCount = len(nums)
        while outerIndex < nCount:
            currentNum = nums[outerIndex]
            multiples = generateMultiples(currentNum, threshold)
            innerIndex = 0
            multCount = len(multiples)
            while innerIndex < multCount:
                dsu.union_set(currentNum, multiples[innerIndex])
                innerIndex += 1
            outerIndex += 1

        resultSet = set()
        i = 0
        while i < nCount:
            val = nums[i]
            if val <= threshold:
                resultSet.add(dsu.find(val))
            else:
                resultSet.add(val)
            i += 1

        return len(resultSet)