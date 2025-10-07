class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        accumulated = 0
        scraps = 0
        while True:
            if numBottles <= 0:
                break
            accumulated += numBottles
            scraps += numBottles
            numBottles = 0
            while scraps >= numExchange:
                scraps -= numExchange
                numBottles += 1
                numExchange += 1
        return accumulated