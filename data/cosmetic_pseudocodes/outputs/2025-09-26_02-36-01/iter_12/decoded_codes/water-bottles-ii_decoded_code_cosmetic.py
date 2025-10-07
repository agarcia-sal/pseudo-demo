class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        def sub_collectNewBottles(currentEmpty: int, exchangeLimit: int):
            if not (currentEmpty < exchangeLimit):
                updatedEmpty = currentEmpty - exchangeLimit
                refreshedBottles = 1

                nextEmpty = updatedEmpty
                nextLimit = exchangeLimit + 1

                remainingEmpty, totalNewBottles = sub_collectNewBottles(nextEmpty, nextLimit)
                totalNewBottles += refreshedBottles

                return [remainingEmpty, totalNewBottles]
            else:
                return [currentEmpty, 0]

        cumulativeConsumed = 0
        recyclableEmpties = 0

        while numBottles > 0:
            cumulativeConsumed += numBottles
            recyclableEmpties += numBottles
            numBottles = 0

            recyclableEmpties, numBottles = sub_collectNewBottles(recyclableEmpties, numExchange)

        return cumulativeConsumed