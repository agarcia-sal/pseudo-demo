class DSU:
    def __init__(self, n):
        parentMap = {}
        rankMap = {}
        localIndex = 0
        while localIndex < n:
            parentMap[localIndex] = localIndex
            rankMap[localIndex] = 1
            localIndex += 1
        self.parent = parentMap
        self.rank = rankMap

    def find(self, x):
        locVarA = self.parent[x]
        if locVarA != x:
            self.parent[x] = self.find(locVarA)
        return self.parent[x]

    def union_set(self, u, v):
        firstRoot = self.find(u)
        secondRoot = self.find(v)
        if firstRoot != secondRoot:
            rankFirst = self.rank[firstRoot]
            rankSecond = self.rank[secondRoot]

            if not (rankFirst >= rankSecond):
                swapVar = firstRoot
                firstRoot = secondRoot
                secondRoot = swapVar

            self.parent[secondRoot] = firstRoot
            if self.rank[firstRoot] == self.rank[secondRoot]:
                self.rank[firstRoot] += 1


class Solution:
    def countComponents(self, nums, threshold):
        dsuInstance = DSU(threshold + 1)
        iterIndex = 0
        while True:
            if iterIndex >= len(nums):
                break
            outerElement = nums[iterIndex]

            innerElement = outerElement * 2
            while innerElement <= threshold:
                dsuInstance.union_set(outerElement, innerElement)
                innerElement += outerElement

            iterIndex += 1

        uniqueRoots = set()
        for outerElement in nums:
            if outerElement <= threshold:
                uniqueRoots.add(dsuInstance.find(outerElement))
            else:
                uniqueRoots.add(outerElement)

        return len(uniqueRoots)