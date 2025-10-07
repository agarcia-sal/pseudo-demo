class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        consumed_sum = 0
        spent_containers = 0
        while numBottles > 0:
            consumed_sum += numBottles
            spent_containers += numBottles
            numBottles = 0
            while spent_containers >= numExchange:
                spent_containers -= numExchange
                numBottles += 1
                numExchange += 1
        return consumed_sum