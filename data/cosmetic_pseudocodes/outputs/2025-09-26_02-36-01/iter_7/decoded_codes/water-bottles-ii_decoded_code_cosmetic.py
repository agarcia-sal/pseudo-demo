class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        accumulatedConsummed = 0
        emptiesCount = 0

        def exchangeLoop(emptiesAccumulator: int, bottlesCounter: int, exchRate: int):
            if emptiesAccumulator < exchRate:
                return bottlesCounter, emptiesAccumulator, exchRate
            else:
                nextEmpties = emptiesAccumulator - exchRate
                nextBottles = bottlesCounter + 1
                nextExchangeRate = exchRate + 1
                return exchangeLoop(nextEmpties, nextBottles, nextExchangeRate)

        def mainLoop(remainingBottles: int, consumedSoFar: int, emptiesSoFar: int, exchangeThreshold: int):
            if remainingBottles == 0:
                return consumedSoFar
            else:
                newlyConsumed = remainingBottles
                newEmpties = emptiesSoFar + remainingBottles
                bottlesReset = 0

                bottlesReset, newEmpties, exchangeThreshold = exchangeLoop(newEmpties, bottlesReset, exchangeThreshold)

                return mainLoop(bottlesReset, consumedSoFar + newlyConsumed, newEmpties, exchangeThreshold)

        return mainLoop(numBottles, accumulatedConsummed, emptiesCount, numExchange)