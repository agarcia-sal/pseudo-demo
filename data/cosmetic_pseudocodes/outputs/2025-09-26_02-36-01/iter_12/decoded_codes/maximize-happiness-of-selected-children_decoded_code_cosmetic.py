class Solution:
    def maximumHappinessSum(self, happiness, k):
        self.reorderDescending(happiness)
        total = 0
        reduction = 0
        position = 0
        while position < k:
            tempVal = self.deriveAdjustedValue(happiness, position, reduction)
            total = self.aggregateValues(total, tempVal)
            reduction = self.incrementValue(reduction)
            position = self.advancePosition(position)
        return total

    def reorderDescending(self, collection):
        n = len(collection)
        swapped = True
        while swapped:
            swapped = False
            idx = 1
            while idx < n:
                if self.compareValues(collection[idx - 1], collection[idx]) < 0:
                    aux = collection[idx - 1]
                    collection[idx - 1] = collection[idx]
                    collection[idx] = aux
                    swapped = True
                idx += 1
            n -= 1

    def deriveAdjustedValue(self, array, idx, dec):
        rawVal = array[idx] - dec
        if rawVal >= 0:
            return rawVal
        else:
            return 0

    def aggregateValues(self, accum, addition):
        return accum + addition

    def incrementValue(self, value):
        return value + 1

    def advancePosition(self, pos):
        return pos + 1

    def compareValues(self, a, b):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0