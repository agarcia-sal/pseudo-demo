from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours):
        remainderCount = defaultdict(int)
        totalPairs = 0
        for hour in hours:
            currentRemainder = hour % 24
            neededRemainder = (24 - currentRemainder) % 24
            totalPairs += remainderCount[neededRemainder]
            remainderCount[currentRemainder] += 1
        return totalPairs