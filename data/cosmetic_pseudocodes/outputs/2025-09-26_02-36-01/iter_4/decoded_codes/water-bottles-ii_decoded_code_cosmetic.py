class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        consumed_total = 0
        bottles_emptied = 0
        while numBottles > 0:
            consumed_total += numBottles
            bottles_emptied += numBottles
            numBottles = 0
            while bottles_emptied >= numExchange:
                bottles_emptied -= numExchange
                numBottles += 1
                numExchange += 1
        return consumed_total