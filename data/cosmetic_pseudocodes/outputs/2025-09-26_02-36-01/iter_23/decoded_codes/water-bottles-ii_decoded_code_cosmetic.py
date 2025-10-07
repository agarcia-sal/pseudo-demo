class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        def recursiveDrink(consumed: int, empties: int, currentBottles: int) -> int:
            if currentBottles > 0:
                newConsumed = consumed + currentBottles
                newEmpties = empties + currentBottles
                currentBottles = 0

                def innerExchange(exchCount: int, bottlesNow: int, empt: int):
                    if empt < exchCount:
                        return bottlesNow, empt
                    empt -= exchCount
                    bottlesNow += 1
                    exchCount += 1
                    return innerExchange(exchCount, bottlesNow, empt)

                updatedBottles, updatedEmpties = innerExchange(numExchange, currentBottles, newEmpties)
                return recursiveDrink(newConsumed, updatedEmpties, updatedBottles)
            else:
                return consumed

        consumed_sum = 0
        bottles_empty = 0
        consumed_sum = recursiveDrink(consumed_sum, bottles_empty, numBottles)
        return consumed_sum