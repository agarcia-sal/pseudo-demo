class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        def subtractAndReturn(a, b):
            return a - b

        def addValues(a, b):
            return a + b

        def isGreater(x, y):
            return x > y

        def isAtLeast(x, y):
            return x >= y

        alpha = 0
        beta = 0

        while isGreater(numBottles, 0):
            alpha = addValues(alpha, numBottles)
            beta = addValues(beta, numBottles)
            numBottles = subtractAndReturn(numBottles, numBottles)  # sets to 0

            while isAtLeast(beta, numExchange):
                beta = subtractAndReturn(beta, numExchange)
                numBottles = addValues(numBottles, 1)
                numExchange = addValues(numExchange, 1)

        return alpha