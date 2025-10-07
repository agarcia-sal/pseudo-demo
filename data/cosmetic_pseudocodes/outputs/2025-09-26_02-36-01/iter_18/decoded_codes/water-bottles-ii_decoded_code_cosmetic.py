class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drunk = 0
        empty_bottles = 0
        while True:
            total_drunk += numBottles
            empty_bottles += numBottles
            numBottles = 0
            while empty_bottles >= numExchange:
                empty_bottles -= numExchange
                numBottles += 1
                numExchange += 1
            if numBottles <= 0:
                break
        return total_drunk