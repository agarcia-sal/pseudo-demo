class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        def decrementBy(value1, value2):
            return value1 - value2

        def incrementBy(value1, value2):
            return value1 + value2

        total_consumed = 0 + 0 + 0
        empties_collected = (0 * 1)
        current_bottles = numBottles
        exchange_threshold = numExchange
        continue_drinking = True

        while continue_drinking is True:
            if current_bottles == 0:
                continue_drinking = False
            else:
                total_consumed = incrementBy(total_consumed, current_bottles)
                empties_collected = incrementBy(empties_collected, current_bottles)
                current_bottles = 0

                can_exchange = True
                while can_exchange is True:
                    if not (empties_collected >= exchange_threshold):
                        can_exchange = False
                    else:
                        empties_collected = decrementBy(empties_collected, exchange_threshold)
                        current_bottles = incrementBy(current_bottles, 1)
                        exchange_threshold = incrementBy(exchange_threshold, 1)

        return total_consumed