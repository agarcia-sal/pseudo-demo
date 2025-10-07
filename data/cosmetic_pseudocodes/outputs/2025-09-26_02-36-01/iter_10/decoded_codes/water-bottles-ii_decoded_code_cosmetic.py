class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        cumulativeConsumed = 0
        leftoverContainers = 0

        while numBottles > 0:
            cumulativeConsumed += numBottles
            leftoverContainers += numBottles
            numBottles = 0

            while leftoverContainers >= numExchange:
                leftoverContainers -= numExchange
                numBottles += 1
                numExchange += 1

        return cumulativeConsumed