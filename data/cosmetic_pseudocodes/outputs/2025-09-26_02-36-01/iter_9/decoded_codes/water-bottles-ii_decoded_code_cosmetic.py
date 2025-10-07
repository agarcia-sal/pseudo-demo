class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        def calcNewBottles(consumed: int, empties: int, exchangeRate: int) -> int:
            gained = 0
            rest = empties
            while True:
                if rest < exchangeRate:
                    break
                rest -= exchangeRate
                gained += 1
                rest += 1
            return gained

        aggregateDrank = 0
        residualEmpties = 0

        while numBottles > 0:
            aggregateDrank += numBottles
            residualEmpties += numBottles
            numBottles = 0

            while residualEmpties >= numExchange:
                residualEmpties -= numExchange
                numBottles += 1
                numExchange += 1

        return aggregateDrank