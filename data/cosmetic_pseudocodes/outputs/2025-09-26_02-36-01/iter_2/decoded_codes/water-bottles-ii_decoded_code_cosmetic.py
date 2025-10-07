class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        totalConsumed = 0
        empties = 0
        while numBottles > 0:
            totalConsumed += numBottles
            empties += numBottles
            numBottles = 0
            while empties >= numExchange:
                empties -= numExchange
                numBottles += 1
                numExchange += 1
        return totalConsumed