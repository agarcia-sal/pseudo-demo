class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        countConsumed = 0
        bottlesEmpty = 0
        while True:
            if not (numBottles > 0):
                break
            countConsumed += numBottles
            bottlesEmpty += numBottles
            numBottles = 0
            while numExchange <= bottlesEmpty:
                bottlesEmpty -= numExchange
                numBottles += 1
                numExchange += 1
        return countConsumed