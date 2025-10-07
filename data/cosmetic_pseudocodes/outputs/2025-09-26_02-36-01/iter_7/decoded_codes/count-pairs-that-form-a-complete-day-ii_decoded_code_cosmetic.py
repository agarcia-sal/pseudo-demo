from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours):
        residueFrequency = defaultdict(int)
        totalPairs = 0
        idx = 0
        n = len(hours)
        while idx < n:
            currentHour = hours[idx]
            modValue = currentHour % 24
            inverseResidue = (24 - modValue) % 24
            totalPairs += residueFrequency[inverseResidue]
            residueFrequency[modValue] += 1
            idx += 1
        return totalPairs