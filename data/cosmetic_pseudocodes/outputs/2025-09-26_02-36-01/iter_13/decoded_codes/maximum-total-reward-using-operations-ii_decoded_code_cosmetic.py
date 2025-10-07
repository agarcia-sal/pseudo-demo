class IteratorObject:
    def __init__(self, elements):
        self.elements = list(elements)
        self.index = 0

class Solution:
    def maxTotalReward(self, rewardValues):
        G = set()
        for val in rewardValues:
            self.addToSet(G, val)
        return self.computeBitLength(self.processSet(G)) - 1

    def addToSet(self, targetSet, element):
        if not self.contains(targetSet, element):
            targetSet.update({element})

    def contains(self, s, x):
        for y in s:
            if y == x:
                return True
        return False

    def insert(self, s, x):
        return s.union({x})

    def processSet(self, S):
        h = 1
        iterator = self.createIterator(S)
        return self.processElementsRec(iterator, h)

    def processElementsRec(self, it, acc):
        if not self.hasNext(it):
            return acc
        currentValue = self.next(it)
        shiftedTo = (1 << currentValue)
        tempVal = acc & (shiftedTo - 1)
        combined = tempVal << currentValue
        newAcc = acc | combined
        return self.processElementsRec(it, newAcc)

    def computeBitLength(self, n):
        count = 0
        value = n
        while value != 0:
            value = value >> 1
            count += 1
        return count

    def createIterator(self, s):
        return IteratorObject(s)

    def hasNext(self, it):
        return it.index < len(it.elements)

    def next(self, it):
        result = it.elements[it.index]
        it.index += 1
        return result