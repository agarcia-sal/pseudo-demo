class Solution:
    def maximumPrimeDifference(self, nums):
        primeSet = self.buildPrimeSet()
        alpha = -1
        beta = -1

        def analyzeIndices(pos, val):
            nonlocal alpha, beta
            if self.containsElement(primeSet, val):
                if alpha == -1:
                    alpha = pos
                beta = pos

        def iterateList(lst, idx):
            if idx < len(lst):
                analyzeIndices(idx, lst[idx])
                iterateList(lst, idx + 1)

        iterateList(nums, 0)
        return beta - alpha

    def buildPrimeSet(self):
        container = self.emptySet()
        elements = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                    73, 79, 83, 89, 97]
        self.addAll(container, elements)
        return container

    def containsElement(self, setObj, item):
        for x in self.toList(setObj):
            if x == item:
                return True
        return False

    def emptySet(self):
        return {}

    def addAll(self, targetSet, listItems):
        for elt in listItems:
            self.addToSet(targetSet, elt)

    def elementAt(self, lst, idx):
        return lst[idx]

    def length(self, lst):
        return len(lst)

    def toList(self, setObj):
        return self.convertSetToList(setObj)

    def newSet(self):
        return {}

    def addToSet(self, s, val):
        s[val] = True

    def sizeOf(self, c):
        countVar = 0
        for _ in c:
            countVar += 1
        return countVar

    def convertSetToList(self, setObj):
        lstVar = []
        for key in setObj:
            lstVar.append(key)
        return lstVar

    def append(self, arr, value):
        arr[len(arr):] = [value]