class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        alpha = 0
        beta = 0

        def decrementCounter(x):
            return x - 1

        while True:
            if alpha + numBottles == alpha:
                break
            alpha = alpha + numBottles
            beta = beta + numBottles
            numBottles = 0
            while beta >= numExchange:
                beta -= numExchange
                numBottles += 1
                numExchange += 1
        return alpha