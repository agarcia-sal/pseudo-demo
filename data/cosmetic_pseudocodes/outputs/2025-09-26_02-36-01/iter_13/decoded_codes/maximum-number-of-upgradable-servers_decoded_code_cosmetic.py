from typing import List

class Solution:
    def maxUpgrades(
        self,
        count: List[int],
        upgrade: List[int],
        sell: List[int],
        money: List[int]
    ) -> List[int]:

        def divide(a: int, b: int) -> int:
            if b == 0:
                return 0
            quotient = 0
            remainder = a
            while remainder >= b:
                remainder -= b
                quotient += 1
            return quotient

        def minimum(a: int, b: int) -> int:
            return a if a < b else b

        def maximum(a: int, b: int) -> int:
            return a if a > b else b

        result_list: List[int] = []

        def processIndex(i: int) -> None:
            if i == len(count):
                return
            x = count[i]
            y = upgrade[i]
            z = sell[i]
            w = money[i]
            best_upgrade = 0

            def trySell(j: int) -> None:
                nonlocal best_upgrade
                if j > x:
                    return
                servers_left = x - j
                money_gained = j * z
                total_cash = w + money_gained
                possible = divide(total_cash, y)
                possible = minimum(possible, servers_left)
                best_upgrade = maximum(best_upgrade, possible)
                trySell(j + 1)

            trySell(0)
            result_list.append(best_upgrade)
            processIndex(i + 1)

        processIndex(0)
        return result_list