class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        output_total = 0
        collector_empty = 0

        while numBottles > 0:
            output_total += numBottles
            collector_empty += numBottles
            numBottles = 0
            while collector_empty >= numExchange:
                collector_empty -= numExchange
                numBottles += 1
        return output_total