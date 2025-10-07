class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        totalConsumed = 0
        empties = 0

        while True:
            if numBottles == 0:
                break
            totalConsumed += numBottles
            empties += numBottles
            numBottles = 0

            while empties >= numExchange:
                empties -= numExchange
                numBottles += 1
                numExchange += 1

        return totalConsumed