class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        s_alpha = 0
        t_zeta = 0
        while True:
            if numBottles <= 0:
                break
            s_alpha += numBottles
            t_zeta += numBottles
            numBottles = 0
            while t_zeta >= numExchange:
                t_zeta -= numExchange
                numBottles += 1
                numExchange += 1
        return s_alpha