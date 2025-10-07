class Solution:
    def maximumHappinessSum(self, happiness, k):
        sortedList = sorted(happiness, reverse=True)
        total = 0
        reduceBy = 0
        for i in range(k):
            adjustedValue = sortedList[i] - reduceBy
            if adjustedValue < 0:
                adjustedValue = 0
            total += adjustedValue
            reduceBy += 1
        return total