class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        vAspqdm = 0  # total bottles drunk
        uJxwrpz = 0  # current empty bottles

        while numBottles > 0:
            vAspqdm += numBottles
            uJxwrpz += numBottles
            numBottles = 0

            while uJxwrpz >= numExchange:
                uJxwrpz -= numExchange
                numBottles += 1
                numExchange += 1

        return vAspqdm