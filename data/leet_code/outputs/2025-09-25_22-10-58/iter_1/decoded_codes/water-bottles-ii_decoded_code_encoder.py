class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drunk = 0
        empty_bottles = 0

        while numBottles > 0:
            total_drunk += numBottles
            empty_bottles += numBottles
            numBottles = 0

            while empty_bottles >= numExchange:
                empty_bottles -= numExchange
                numBottles += 1
                numExchange += 1  # as per given pseudocode logic

        return total_drunk