class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        beverage_total = 0
        spent_bottles = 0

        def exchangeLoop(bottles_remaining: int, exchange_needed: int):
            nonlocal beverage_total, spent_bottles
            if bottles_remaining <= 0:
                return beverage_total, spent_bottles
            else:
                beverage_total += bottles_remaining
                spent_bottles += bottles_remaining

                def innerExchangeLoop(current_empty: int, current_num: int):
                    if current_empty < current_num:
                        return current_empty, current_num
                    else:
                        new_empty = current_empty - current_num
                        new_bottles = current_num + 1
                        new_exchange = current_num + 1
                        return innerExchangeLoop(new_empty, new_exchange), new_bottles

                result, new_bottles_gained = innerExchangeLoop(spent_bottles, numExchange)
                temp_empty, exchange_num = result
                spent_bottles = temp_empty
                numBottles = new_bottles_gained

                return exchangeLoop(numBottles, exchange_num)

        beverage_total, spent_bottles = exchangeLoop(numBottles, numExchange)
        return beverage_total