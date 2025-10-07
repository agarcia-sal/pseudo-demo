class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        p1 = 0
        p2 = 0
        while numBottles > 0:
            p1 += numBottles
            p2 += numBottles
            numBottles = 0
            while p2 >= numExchange:
                p2 -= numExchange
                numBottles += 1
                numExchange += 1
        return p1