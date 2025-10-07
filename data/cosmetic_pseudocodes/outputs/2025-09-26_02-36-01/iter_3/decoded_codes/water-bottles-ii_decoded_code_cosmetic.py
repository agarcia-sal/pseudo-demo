class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        consumedCount = 0
        empties = 0
        while numBottles != 0:
            consumedCount += numBottles
            empties += numBottles
            numBottles = 0
            while empties >= numExchange:
                empties -= numExchange
                numBottles += 1
                numExchange += 1
        return consumedCount