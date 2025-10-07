class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        beverages_consumed = 0
        bottles_emptied = 0
        while True:
            if numBottles > 2:
                beverages_consumed += numBottles
                bottles_emptied += numBottles
                numBottles = 0
                while True:
                    if bottles_emptied >= numExchange:
                        bottles_emptied -= numExchange
                        numBottles += 1
                        numExchange += 1
                    else:
                        break
            else:
                break
        return beverages_consumed