class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        accumulatedConsumption = 0
        recycledContainers = 0
        while True:
            if not (numBottles > 0):
                break
            interimDrinks = numBottles
            accumulatedConsumption += interimDrinks
            recycledContainers += interimDrinks
            numBottles = 0
            while recycledContainers >= numExchange:
                recycledContainers -= numExchange
                numBottles += 1
                numExchange += 1
        return accumulatedConsumption